#! /bin/sh
# chkconfig: 2345 95 20
# description: Django Start|Stop|Restart
# Script para o Servico FCGI do Django.
# processname: fcgi

PROCESSNAME="fcgi"

DJANGO_SETTINGS="myproject.settings"

FCGI_PATH="~/fcgi"
FCGI_LOG="~/logs"
NGINX_PATH="~/nginx"

if [ ! -d $FCGI_PATH ]; then
  mkdir -p $FCGI_PATH
fi

if [ ! -d $FCGI_LOG ]; then
  mkdir -p $FCGI_LOG
fi

if [ ! -d $NGINX_PATH ]; then
  mkdir -p $NGINX_PATH
fi

P=$FCGI_PATH/fcgi.pid
S=$FCGI_PATH/fcgi.sock
E=$FCGI_LOG/fcgi.errlog
O=$FCGI_LOG/fcgi.outlog

start(){
  sudo chmod -R 777 $FCGI_PATH
  sudo chmod -R 777 $FCGI_LOG

  python manage.py runfcgi daemonize=true \
                           maxchildren=10 \
                           maxspare=5 \
                           minspare=2 \
                           method=prefork \
                           socket=$S \
                           pidfile=$P \
                           errlog=$E \
                           outlog=$O \
                           --settings=$DJANGO_SETTINGS && chmod 777 $S
}

stop(){
  sudo kill -9 `pidof python`
}

restart(){
  stop
  start
}

status(){
  pidof python
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    restart
    ;;
  status)
    status
    ;;
  *)
    echo "Usage: $1 {start|stop|restart|status}" 
    exit 1
    ;;
esac

exit 0
