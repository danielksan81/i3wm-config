from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",
                format=('%b %a %d %H:%M:%S', 'Europe/Berlin'),)

# Shows the average load of the last minute and the last 5 minutes using default format
status.register("load")

status.register('cpu_usage')

status.register("mem",
                divisor=1073741824,
                format="{used_mem}G/{total_mem}G")

status.register("network",
                interface="eth0",
                format_up="{v4cidr}|{bytes_recv:5.0f}|{bytes_sent:4.0f}",
                dynamic_color=False,
                format_down="")

#status.register("network",
#                interface="wlan0",
#                format_up="{v4cidr} {essid} {quality}|" +
#                          "{bytes_recv:5.0f}|{bytes_sent:4.0f}",
#                dynamic_color=False,
#                format_down="",)

status.register("disk",
                path="/mnt/dev/",
                format="dev {avail:.1f}G",)

status.register("disk",
                path="/",
                format="/ {avail:.1f}G",)

status.run()
