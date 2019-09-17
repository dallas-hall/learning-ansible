# Create Ambari Cluster

This role configures a vanilla Fedora Desktop installation to the way I like it.

## Requirements

* An Ansible playbook and inventory file that configures which hosts will be touched.

## Role Variables

- `/path/to/ansible/inventory/hosts.yml` - The inventory file of the cluster.
- `defaults/main.yml` - Has variables that are used by tasks and templates throughout the role. This is the main place to update to change the data the role works with.
- `templates/templates/bashrc-root.j2` - Customisations for the `root` account `.bashrc`
- `templates/templates/bashrc-user.j2` - Customisations for the user account `.bashrc`
- `tasks/*` - The things that this role does.

## Example Playbook

* `/path/to/ansible/master-playbook.yml`

```yaml
---
- name: Configure Fedora to my liking.
  hosts: localhost
  become: yes
  gather_facts: yes
  roles:
  	- fedora-post-installation-configuration
```

* `ansible-playbook -i /path/to/ansible/inventory/hosts.yml master-playbook.yml -K`

## License

MIT License

Copyright (c) 2019 blindcant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author Information

blindcant
