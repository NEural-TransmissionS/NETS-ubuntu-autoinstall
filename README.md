# NETS Ubuntu autoinstall ISO builder

This repo uses pxeless to build an unattended autoinstall Ubuntu ISO for NETS lab use.


## Usage
By default (without repo secret), the pipeline will build ISO for Ubuntu 22.04 LTS or 20.04 LTS with the following configuration:
- Username: `ubuntu`, Password: `ubuntu`, Hostname: `ubuntu-server`
- Install OpenSSH server
- Use `/dev/nvme0n1` (First NVMe drive) for LVM
- Passwordless `sudo`
- NVIDIA headless driver

To customize the ISO:
- Create a hashed password using `mkpasswd -m sha512crypt`
- Fork this repo and add the following secrets to your repo action secrets `JINJA_CONFIG`:
```json
{
    "username": "johndoe",
    "hostname": "example-host",
    "hashed_password": "hashedpassword",
    "luks_key": "lukskey",
    "ubuntu_pro_token": "ubuntuprotoken",
    "ssh_pubkey": "ssh-rsa ...",
    "github_username": "johndoe",
    "netbird_setupkey": "NETBIRD_KEY",
    "netbird_url": "NETBIRD_URL"
}
```

## Explanation:
- `username`, `hostname`, `hashed_password`: Self-explanatory
- (Recommended) `luks_key`: passphrase for Full Disk Encryption (FDE) for LVM root partition
- (Recommended) `ssh_pubkey`: SSH public key for login, disable password login
- (Optional) `ubuntu_pro_token`: Ubuntu Pro token for Canonical Livepatch
- (Optional) `github_username`: GitHub username for SSH `authorized_keys` instead of explicit `ssh_pubkey`, disable password login
- (Optional) `netbird_setupkey`, `netbird_url`: Netbird setup key and management URL for remote management.