from bcc import BPF
from time import sleep

# eBPF program
bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>

BPF_PERF_OUTPUT(events);

struct data_t {
    u32 pid;
    u32 uid;
    char comm[TASK_COMM_LEN];
    char filename[256];
    u64 arg1;
    u64 arg2;
    u64 arg3;
    u64 arg4;
};

int trace_openat(struct pt_regs *ctx) {
    struct data_t data = {};
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    u32 uid = bpf_get_current_uid_gid();
   
    const char __user *filename = (const char __user *)PT_REGS_PARM2(ctx);
    data.pid = pid;
    data.uid = uid;
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    data.arg1=PT_REGS_PARM1(ctx);
    data.arg2=PT_REGS_PARM2(ctx);
    data.arg3=PT_REGS_PARM3(ctx);
    data.arg4=PT_REGS_PARM4(ctx);
    bpf_probe_read_user(&data.filename, sizeof(data.filename), filename);

    events.perf_submit(ctx, &data, sizeof(data));
    return 0;
}
"""

# Load BPF program
bpf = BPF(text=bpf_text)
bpf.attach_kprobe(event="__x64_sys_openat", fn_name="trace_openat")
tracked_commands={"touch","echo","cat","cp","mv","rm"}
# Callback function to print output
def print_event(cpu, data, size):
    event = bpf["events"].event(data)
    
    command=event.comm.decode('utf-8','ignore')
    filename=event.filename.decode('utf-8','ignore')
    if command in tracked_commands:
    	print(f"PID: {event.pid}, UID: {event.uid}, CMD: {command}, FILE: {filename}")

# Open perf buffer and start tracing
bpf["events"].open_perf_buffer(print_event)
print("Tracing file creations... Press Ctrl+C to stop.")

try:
    while True:
        bpf.perf_buffer_poll()
except KeyboardInterrupt:
    print("Exiting...")
