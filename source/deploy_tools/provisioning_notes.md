配置新网站
================
## 需要的包:  
* nginx
* Python 3.7
* virtualenv + pip
* Git

以Ubuntu 19.04为例:  
  sudo apt-get install nginx git python37 python3.7-venv

## Nginx虚拟主机
* 参考nginx.teamplate.conf
* 把SITENAME替换成所需的域名, 例如lgzzzz.com

## Systemd服务
* 参考gunicorn-upstart.template.conf
* 把SITENAME替换成所需的域名, 例如lgzzzz.com

## 文件夹结构
假设有用户账户, 家目录为/home/username

/home/username
└── sites
    └── SITENAME 
        ├── database
        ├── source
        ├── static
        └── virtualenv

