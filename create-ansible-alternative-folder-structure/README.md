# Overview
This Ansible playbook will:
* Set up a simplified version of the [Ansible best practice alternative directory structure](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#alternative-directory-layout) that also uses the [Ansible Role directory structure](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#role-directory-structure).
* Copy some files:
  * `hosts.yml` with localhost defined.

Before running, update the values inside of
* `./roles/localhost/vars/main.yml` to suit your needs.
  * Uncomment anything you need to comment out anything you dont.
  * In `my_roles` leave in common as this covers every group and host.
* `./roles/localhost/files/` has the files that will be copied.
  * `master-playbook.yml`
  * `inventories/hosts.ini`
* `./roles/localhost/tasks/`
  * `copy-files.yml` for any files you have added inside `./roles/localhost/files/`

Execute with `ansible-playbook master-playbook.yml -i inventories/localhost/hosts.ini`

The execution flow is
* `master-playbook.yml`
* `inventories/*`
* `roles/localhost/main.yml`
