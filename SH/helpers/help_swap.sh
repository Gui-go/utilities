


# Swappiness refers to the kernel parameter responsible for how much and how often that the system moves data from RAM to swap memory.
cat /proc/sys/vm/swappiness

# Change swappiness
sudo sysctl vm.swappiness=x

free -m 

# Turn off memory swap
swapoff -a

# Turn on memory swap
swapon -a


vmstat 1

top

htop


