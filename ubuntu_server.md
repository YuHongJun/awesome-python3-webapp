# 开启root账号
`demi817@ubuntu:~$` => `root@ubuntu:/home/demi817#`

sudo passwd root #启用root账号并设置密码
su root #从普通用户切换到root账号
sudo passwd -l root #禁用root账号，如果要启用重新走第一步


# 设置IP地址,网关,DNS

`root@ubuntu:/home/demi817#`  nano /etc/network/interfaces #编辑网卡配置文件

```
auto lo
iface lo inet loopback

# The primary network interface
auto enp0s3
iface enp0s3 inet static
address 192.168.13.3    #要和主机在一个网段 192.168.13.XXX
netmask 255.255.255.0
gateway 192.168.13.159  #主机物理ip
dns-nameservers 192.168.13.159
dns-nameservers 8.8.8.8

```

ctrl+o #保存配置

ctrl+x #退出

sudo /etc/init.d/networking restart  #重启网络
service networking restart #重新启动网络

# 设置DNS

nano /etc/resolv.conf

nameserver 192.168.13.159

nameserver 8.8.8.8

nameserver 8.8.8.8
ctrl+o

ctrl+x


ifconfig enp0s3

基本的排错步骤（从上往下）
ping 127.0.0.1ping的通说明tcp协议栈没有问题
ping 192.168.13.159    主机地址 ping的通说明网卡没有问题
ping 192.168.13.1 路由器默认网关 ping的通说明包可以到达路由器
最后 ping 8.8.8.8 DNS服务器地址
卡在那一步，就补哪里












