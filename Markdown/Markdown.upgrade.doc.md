# Doc about Upgrade for Kubeadm

---

1. ## Requirements

    - access point to vpn with: kubelet, kubectl and kubeadm installed [^0]

    - cluster of machines, with: least one master and some other nodes as workers (least one worker)



2. ## Sources

    - official page : [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)



3. ## Steps

    1. ### [Check](#check) the current version
    2. ### [Drain](#drain) machines
    3. ### [Install](#install) the newest version
    3. ### [Restart](#restart) machines' services
    4. ### [Uncordon](#uncordon) machines

---

1. ## Check the current version {#check}

    official page for see the newest version :
      [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

    ### Commands

       1. ~$ *kubeadm version* [^1]



2. ## Drain machines {#drain}

    only for not main master(s) and worker(s)

    to execute on localhost or into master(s)

    ### Commands

       1. ~$ *kubectl drain <...\> --ignore-daemonsets* [^2]

       2. to fix the bug on drain for the occupated nodes by pods:

          ~$ *kubectl drain <...\> --ignore-daemonset --delete-emptydir-data* [^3]

    ### Machines

       - X can be master(s) or worker(s)

       - you can get a list of available nodes using:

          1. ~$ *kubectl get nodes* [^4]



3. ## Install the software {#install}

    inside every machines (nodes) to upgrade

    ### Commands [^5]

       1. ~$ *sudo -i*

       2. ~$ *apt-get update && apt-get install -y --allow-change-held-packages kubeadm=...*

       3. ~$ *kubeadm version*

       4. ~$ *kubeadm upgrade node*

       5. ~$ *apt-get update && \
              apt-get install -y --allow-change-held-packages kubelet=... kubectl=...*



4. ## Restart the machines' server {#restart}

    ### Commands [^6]

       1. ~$ *systemctl daemon-reload*

       2. ~$ *systemctl restart kubelet*



5. ## Uncordon machines {#uncordon}

    only for not main master(s) and worker(s)

    to execute on localhost or into master(s)

    ### Commands

       1. ~$ *kubectl uncordon <...\>* [^7]

---

## Notes

[^0]: Usually called localhost for our docker environment, it's able to reach vpn system using host configuration .
      Like mentioned before it requires: kubelet, kubectl and kubeadm installed.

[^1]: Command to execute for get the version of kubeadm.

[^2]: You can use kubectl drain to safely evict all of your pods from a node before you perform maintenance on the node
      (e.g. kernel upgrade, hardware maintenance, etc.). It will close the node for the kubernetes network.

[^3]: --delete-emptydir-data : used to unlock the busy nodes, after that it will be possible drain they correctly.

[^4]: Command to execute for get a list of nodes and its stats.

[^5]: A ordered list of commands written for make upgrade, they are to execute inside the machines (nodes),
      You can reach machines using ssh, example: ssh <user\>@<name-of-nodes\> .

[^6]: A ordered list of commands written for restart the machines (nodes),
      You can reach machines using ssh, example: ssh <user\>@<name-of-nodes\> .

[^7]: Command to execute for connect again the machines (nodes) to the kubernetes network.
