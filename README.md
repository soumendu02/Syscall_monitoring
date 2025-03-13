### Details of Linux 

```bash
cat /etc/os-release

PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

### Kernel version

```bash
uname -r

6.8.0-52-generic
```

### Required packages

```bash
sudo apt install -y clang llvm libelf-dev libbpf-dev linux-headers-$(uname -r) gcc make

sudo apt install -y bpftool

sudo apt install -y bpfcc-tools libbpfcc-dev python3-bpfcc

```
