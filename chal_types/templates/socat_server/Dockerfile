FROM debian:8.0
MAINTAINER {{ author }}
LABEL Description="{{ challenge }}" VERSION='1.0'

#installation
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y socat

RUN adduser --disabled-password --gecos '' {{ chal_name }}
RUN chown -R root:{{ user }} /home/{{ chal_name }}/
RUN chmod 750 /home/{{ chal_name }}
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep

WORKDIR /home/{{ chal_name }}/

{{ files_to_add }}

RUN chown root:{{ chal_name }} /home/{{ chal_name }}/flag
RUN chmod 440 /home/{{ chal_name }}/flag

EXPOSE 8024
CMD ["socat", "-T60", "TCP-LISTEN:8024,reuseaddr,fork,su={{ chal_name }}", "EXEC:/home/{{ chal_name }}/{{ executable }}"]