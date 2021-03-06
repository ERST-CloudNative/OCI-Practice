
随机写：

IOPS: NFS>Block>Local

顺序写：

IOPS: Local>Block>NFS

> 写日志场景，就属于顺序写操作，优先使用块存储


```
# df -HT
Filesystem                                                                                            Type     Size  Used Avail Use% Mounted on
overlay                                                                                               overlay   42G  8.0G   34G  20% /
tmpfs                                                                                                 tmpfs     68M     0   68M   0% /dev
tmpfs                                                                                                 tmpfs    8.3G     0  8.3G   0% /sys/fs/cgroup
shm                                                                                                   tmpfs     68M     0   68M   0% /dev/shm
tmpfs                                                                                                 tmpfs    8.3G   35M  8.3G   1% /etc/hostname
/dev/sdb                                                                                              ext4      53G  122M   50G   1% /opt
/dev/sda3                                                                                             xfs       42G  8.0G   34G  20% /etc/hosts
10.0.10.33:/FileSystem-20220721-0738-02/default-nfs-pv-claim-pvc-839dfd01-6575-4919-adc7-c62d666e07a8 nfs      9.3E   68M  9.3E   1% /usr/share/nginx/html
tmpfs                                                                                                 tmpfs     17G   13k   17G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs                                                                                                 tmpfs    8.3G     0  8.3G   0% /proc/acpi
tmpfs                                                                                                 tmpfs    8.3G     0  8.3G   0% /proc/scsi
tmpfs                                                                                                 tmpfs    8.3G     0  8.3G   0% /sys/firmware
# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 8.03981 s, 5.2 MB/s
# cd /opt
# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 13.1289 s, 3.2 MB/s
# cd /usr/share/nginx/html
# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 27.4994 s, 1.5 MB/s
```

### Local

```
-------------------SIZE:4M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 4MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=10.5MiB/s][r=2697 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=98: Thu Jul 21 09:31:58 2022
  read: IOPS=2856, BW=11.2MiB/s (11.7MB/s)(670MiB/60001msec)
    slat (usec): min=228, max=14938, avg=347.64, stdev=138.64
    clat (usec): min=2, max=109408, avg=44436.90, stdev=3658.14
     lat (usec): min=937, max=110983, avg=44784.83, stdev=3678.97
    clat percentiles (msec):
     |  1.00th=[   41],  5.00th=[   42], 10.00th=[   42], 20.00th=[   43],
     | 30.00th=[   43], 40.00th=[   44], 50.00th=[   44], 60.00th=[   45],
     | 70.00th=[   45], 80.00th=[   46], 90.00th=[   48], 95.00th=[   50],
     | 99.00th=[   56], 99.50th=[   65], 99.90th=[   86], 99.95th=[   99],
     | 99.99th=[  108]
   bw (  KiB/s): min= 8728, max=12152, per=100.00%, avg=11437.96, stdev=494.60, samples=119
   iops        : min= 2182, max= 3038, avg=2859.49, stdev=123.65, samples=119
  lat (usec)   : 4=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=96.46%
  lat (msec)   : 100=3.47%, 250=0.04%
  cpu          : usr=1.70%, sys=6.20%, ctx=171427, majf=0, minf=141
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=171409,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=11.2MiB/s (11.7MB/s), 11.2MiB/s-11.2MiB/s (11.7MB/s-11.7MB/s), io=670MiB (702MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=6629KiB/s][w=1657 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=101: Thu Jul 21 09:32:58 2022
  write: IOPS=1697, BW=6791KiB/s (6954kB/s)(398MiB/60001msec); 0 zone resets
    slat (usec): min=281, max=15717, avg=586.02, stdev=272.12
    clat (usec): min=2, max=117909, avg=74760.98, stdev=6150.53
     lat (usec): min=685, max=118634, avg=75347.34, stdev=6187.36
    clat percentiles (msec):
     |  1.00th=[   64],  5.00th=[   65], 10.00th=[   67], 20.00th=[   70],
     | 30.00th=[   72], 40.00th=[   73], 50.00th=[   75], 60.00th=[   77],
     | 70.00th=[   78], 80.00th=[   80], 90.00th=[   83], 95.00th=[   85],
     | 99.00th=[   90], 99.50th=[   92], 99.90th=[  113], 99.95th=[  116],
     | 99.99th=[  118]
   bw (  KiB/s): min= 5712, max= 7880, per=100.00%, avg=6792.18, stdev=422.90, samples=119
   iops        : min= 1428, max= 1970, avg=1698.04, stdev=105.73, samples=119
  lat (usec)   : 4=0.01%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=0.05%
  lat (msec)   : 100=99.72%, 250=0.20%
  cpu          : usr=1.56%, sys=7.28%, ctx=215442, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,101863,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=6791KiB/s (6954kB/s), 6791KiB/s-6791KiB/s (6954kB/s-6954kB/s), io=398MiB (417MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=48.0MiB/s][r=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=104: Thu Jul 21 09:33:59 2022
  read: IOPS=50, BW=50.3MiB/s (52.8MB/s)(3020MiB/60016msec)
    slat (usec): min=1873, max=29484, avg=19867.51, stdev=3714.23
    clat (usec): min=3, max=2635.7k, avg=2516453.76, stdev=403049.31
     lat (msec): min=19, max=2656, avg=2536.32, stdev=405.05
    clat percentiles (msec):
     |  1.00th=[  456],  5.00th=[ 1603], 10.00th=[ 2635], 20.00th=[ 2635],
     | 30.00th=[ 2635], 40.00th=[ 2635], 50.00th=[ 2635], 60.00th=[ 2635],
     | 70.00th=[ 2635], 80.00th=[ 2635], 90.00th=[ 2635], 95.00th=[ 2635],
     | 99.00th=[ 2635], 99.50th=[ 2635], 99.90th=[ 2635], 99.95th=[ 2635],
     | 99.99th=[ 2635]
   bw (  KiB/s): min=25283, max=51200, per=96.00%, avg=49467.72, stdev=2407.08, samples=119
   iops        : min=   24, max=   50, avg=48.30, stdev= 2.41, samples=119
  lat (usec)   : 4=0.03%
  lat (msec)   : 20=0.03%, 50=0.03%, 100=0.07%, 250=0.26%, 500=0.76%
  lat (msec)   : 750=0.83%, 1000=0.86%, 2000=3.44%, >=2000=93.68%
  cpu          : usr=0.04%, sys=0.38%, ctx=3021, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=3020,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=50.3MiB/s (52.8MB/s), 50.3MiB/s-50.3MiB/s (52.8MB/s-52.8MB/s), io=3020MiB (3167MB), run=60016-60016msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.0MiB/s][w=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=107: Thu Jul 21 09:35:00 2022
  write: IOPS=49, BW=49.0MiB/s (51.4MB/s)(2941MiB/60015msec); 0 zone resets
    slat (usec): min=3145, max=33830, avg=20400.86, stdev=2409.67
    clat (usec): min=3, max=2646.4k, avg=2565841.38, stdev=319209.70
     lat (msec): min=21, max=2666, avg=2586.24, stdev=319.61
    clat percentiles (msec):
     |  1.00th=[  600],  5.00th=[ 2299], 10.00th=[ 2635], 20.00th=[ 2635],
     | 30.00th=[ 2635], 40.00th=[ 2635], 50.00th=[ 2635], 60.00th=[ 2635],
     | 70.00th=[ 2635], 80.00th=[ 2635], 90.00th=[ 2635], 95.00th=[ 2635],
     | 99.00th=[ 2635], 99.50th=[ 2635], 99.90th=[ 2635], 99.95th=[ 2635],
     | 99.99th=[ 2635]
   bw (  KiB/s): min=40960, max=51200, per=98.44%, avg=49399.17, stdev=1085.55, samples=116
   iops        : min=   40, max=   50, avg=48.24, stdev= 1.06, samples=116
  lat (usec)   : 4=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.41%, 750=0.41%
  lat (msec)   : 1000=0.41%, 2000=2.24%, >=2000=96.09%
  cpu          : usr=0.26%, sys=0.50%, ctx=8816, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,2941,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.0MiB/s (51.4MB/s), 49.0MiB/s-49.0MiB/s (51.4MB/s-51.4MB/s), io=2941MiB (3084MB), run=60015-60015msec
-------------------SIZE:8M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 8MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=10.9MiB/s][r=2788 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=110: Thu Jul 21 09:36:01 2022
  read: IOPS=2796, BW=10.9MiB/s (11.5MB/s)(655MiB/60001msec)
    slat (usec): min=234, max=17712, avg=355.07, stdev=155.27
    clat (usec): min=2, max=168227, avg=45387.37, stdev=5149.55
     lat (usec): min=352, max=170975, avg=45742.77, stdev=5182.78
    clat percentiles (msec):
     |  1.00th=[   41],  5.00th=[   43], 10.00th=[   43], 20.00th=[   44],
     | 30.00th=[   44], 40.00th=[   45], 50.00th=[   45], 60.00th=[   46],
     | 70.00th=[   46], 80.00th=[   47], 90.00th=[   49], 95.00th=[   51],
     | 99.00th=[   60], 99.50th=[   73], 99.90th=[  132], 99.95th=[  146],
     | 99.99th=[  161]
   bw (  KiB/s): min= 6512, max=11872, per=100.00%, avg=11191.41, stdev=625.10, samples=119
   iops        : min= 1628, max= 2968, avg=2797.85, stdev=156.28, samples=119
  lat (usec)   : 4=0.01%, 500=0.01%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=94.99%
  lat (msec)   : 100=4.83%, 250=0.14%
  cpu          : usr=1.55%, sys=6.13%, ctx=167834, majf=0, minf=141
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=167807,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=10.9MiB/s (11.5MB/s), 10.9MiB/s-10.9MiB/s (11.5MB/s-11.5MB/s), io=655MiB (687MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=6593KiB/s][w=1648 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=113: Thu Jul 21 09:37:02 2022
  write: IOPS=1720, BW=6880KiB/s (7045kB/s)(403MiB/60003msec); 0 zone resets
    slat (usec): min=280, max=8779, avg=578.26, stdev=247.60
    clat (usec): min=3, max=97999, avg=73792.80, stdev=6614.15
     lat (usec): min=3421, max=98730, avg=74371.41, stdev=6655.17
    clat percentiles (usec):
     |  1.00th=[62653],  5.00th=[64226], 10.00th=[65274], 20.00th=[67634],
     | 30.00th=[69731], 40.00th=[71828], 50.00th=[73925], 60.00th=[74974],
     | 70.00th=[77071], 80.00th=[79168], 90.00th=[82314], 95.00th=[85459],
     | 99.00th=[89654], 99.50th=[90702], 99.90th=[94897], 99.95th=[94897],
     | 99.99th=[96994]
   bw (  KiB/s): min= 5864, max= 7848, per=100.00%, avg=6881.66, stdev=473.90, samples=119
   iops        : min= 1466, max= 1962, avg=1720.41, stdev=118.48, samples=119
  lat (usec)   : 4=0.01%
  lat (msec)   : 4=0.01%, 10=0.01%, 20=0.01%, 50=0.05%, 100=99.92%
  cpu          : usr=1.39%, sys=7.26%, ctx=211603, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,103206,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=6880KiB/s (7045kB/s), 6880KiB/s-6880KiB/s (7045kB/s-7045kB/s), io=403MiB (423MB), run=60003-60003msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=48.0MiB/s][r=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=116: Thu Jul 21 09:38:03 2022
  read: IOPS=49, BW=49.9MiB/s (52.3MB/s)(2994MiB/60017msec)
    slat (usec): min=1904, max=28360, avg=20040.46, stdev=3068.46
    clat (usec): min=5, max=2619.2k, avg=2533374.27, stdev=335753.13
     lat (msec): min=19, max=2639, avg=2553.42, stdev=336.78
    clat percentiles (msec):
     |  1.00th=[  592],  5.00th=[ 2022], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2601], 99.50th=[ 2601], 99.90th=[ 2601], 99.95th=[ 2635],
     | 99.99th=[ 2635]
   bw (  KiB/s): min= 4096, max=51200, per=96.90%, avg=49499.12, stdev=4328.39, samples=118
   iops        : min=    4, max=   50, avg=48.34, stdev= 4.23, samples=118
  lat (usec)   : 10=0.03%
  lat (msec)   : 20=0.03%, 50=0.03%, 100=0.07%, 250=0.27%, 500=0.40%
  lat (msec)   : 750=0.40%, 1000=0.40%, 2000=3.27%, >=2000=95.09%
  cpu          : usr=0.04%, sys=0.29%, ctx=2996, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=2994,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=49.9MiB/s (52.3MB/s), 49.9MiB/s-49.9MiB/s (52.3MB/s-52.3MB/s), io=2994MiB (3139MB), run=60017-60017msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=47.0MiB/s][w=47 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=119: Thu Jul 21 09:39:04 2022
  write: IOPS=49, BW=49.2MiB/s (51.6MB/s)(2954MiB/60018msec); 0 zone resets
    slat (usec): min=3289, max=40149, avg=20312.14, stdev=2420.88
    clat (usec): min=5, max=2638.6k, avg=2554971.72, stdev=317509.45
     lat (msec): min=20, max=2658, avg=2575.28, stdev=317.91
    clat percentiles (msec):
     |  1.00th=[  600],  5.00th=[ 2299], 10.00th=[ 2635], 20.00th=[ 2635],
     | 30.00th=[ 2635], 40.00th=[ 2635], 50.00th=[ 2635], 60.00th=[ 2635],
     | 70.00th=[ 2635], 80.00th=[ 2635], 90.00th=[ 2635], 95.00th=[ 2635],
     | 99.00th=[ 2635], 99.50th=[ 2635], 99.90th=[ 2635], 99.95th=[ 2635],
     | 99.99th=[ 2635]
   bw (  KiB/s): min=43008, max=51200, per=98.44%, avg=49611.03, stdev=1083.24, samples=116
   iops        : min=   42, max=   50, avg=48.45, stdev= 1.06, samples=116
  lat (usec)   : 10=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.41%, 750=0.41%
  lat (msec)   : 1000=0.41%, 2000=2.27%, >=2000=96.07%
  cpu          : usr=0.23%, sys=0.47%, ctx=8854, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,2954,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.2MiB/s (51.6MB/s), 49.2MiB/s-49.2MiB/s (51.6MB/s-51.6MB/s), io=2954MiB (3097MB), run=60018-60018msec
-------------------SIZE:16M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 16MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=11.1MiB/s][r=2830 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=122: Thu Jul 21 09:40:05 2022
  read: IOPS=2777, BW=10.8MiB/s (11.4MB/s)(651MiB/60001msec)
    slat (usec): min=233, max=10732, avg=357.75, stdev=146.64
    clat (nsec): min=1914, max=183701k, avg=45709348.59, stdev=5185759.80
     lat (usec): min=350, max=186504, avg=46067.43, stdev=5219.21
    clat percentiles (msec):
     |  1.00th=[   42],  5.00th=[   43], 10.00th=[   43], 20.00th=[   44],
     | 30.00th=[   45], 40.00th=[   45], 50.00th=[   45], 60.00th=[   46],
     | 70.00th=[   47], 80.00th=[   48], 90.00th=[   49], 95.00th=[   51],
     | 99.00th=[   56], 99.50th=[   66], 99.90th=[  136], 99.95th=[  150],
     | 99.99th=[  171]
   bw (  KiB/s): min= 6256, max=11992, per=100.00%, avg=11112.62, stdev=585.33, samples=119
   iops        : min= 1564, max= 2998, avg=2778.15, stdev=146.34, samples=119
  lat (usec)   : 2=0.01%, 500=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=94.87%
  lat (msec)   : 100=4.90%, 250=0.20%
  cpu          : usr=1.56%, sys=5.88%, ctx=166648, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=166633,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=10.8MiB/s (11.4MB/s), 10.8MiB/s-10.8MiB/s (11.4MB/s-11.4MB/s), io=651MiB (683MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=7332KiB/s][w=1833 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=125: Thu Jul 21 09:41:06 2022
  write: IOPS=1753, BW=7015KiB/s (7184kB/s)(411MiB/60001msec); 0 zone resets
    slat (usec): min=275, max=17763, avg=567.19, stdev=262.97
    clat (usec): min=3, max=100913, avg=72368.94, stdev=5290.30
     lat (usec): min=709, max=101643, avg=72936.48, stdev=5321.22
    clat percentiles (msec):
     |  1.00th=[   62],  5.00th=[   64], 10.00th=[   66], 20.00th=[   69],
     | 30.00th=[   70], 40.00th=[   72], 50.00th=[   73], 60.00th=[   74],
     | 70.00th=[   75], 80.00th=[   77], 90.00th=[   79], 95.00th=[   81],
     | 99.00th=[   86], 99.50th=[   90], 99.90th=[   99], 99.95th=[  101],
     | 99.99th=[  102]
   bw (  KiB/s): min= 5987, max= 8088, per=100.00%, avg=7015.35, stdev=392.89, samples=119
   iops        : min= 1496, max= 2022, avg=1753.83, stdev=98.24, samples=119
  lat (usec)   : 4=0.01%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=0.05%
  lat (msec)   : 100=99.88%, 250=0.04%
  cpu          : usr=1.52%, sys=7.25%, ctx=219893, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,105229,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=7015KiB/s (7184kB/s), 7015KiB/s-7015KiB/s (7184kB/s-7184kB/s), io=411MiB (431MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=48.0MiB/s][r=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=128: Thu Jul 21 09:42:07 2022
  read: IOPS=50, BW=50.2MiB/s (52.6MB/s)(3012MiB/60017msec)
    slat (usec): min=1887, max=23751, avg=19920.98, stdev=3284.44
    clat (usec): min=3, max=2613.6k, avg=2521884.40, stdev=352098.93
     lat (msec): min=21, max=2634, avg=2541.81, stdev=353.47
    clat percentiles (msec):
     |  1.00th=[  617],  5.00th=[ 1888], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2601], 99.50th=[ 2601], 99.90th=[ 2601], 99.95th=[ 2601],
     | 99.99th=[ 2601]
   bw (  KiB/s): min=32768, max=51200, per=96.93%, avg=49811.53, stdev=1872.08, samples=118
   iops        : min=   32, max=   50, avg=48.64, stdev= 1.83, samples=118
  lat (usec)   : 4=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.40%, 750=0.40%
  lat (msec)   : 1000=0.73%, 2000=3.45%, >=2000=94.59%
  cpu          : usr=0.03%, sys=0.27%, ctx=3013, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=3012,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=50.2MiB/s (52.6MB/s), 50.2MiB/s-50.2MiB/s (52.6MB/s-52.6MB/s), io=3012MiB (3158MB), run=60017-60017msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.0MiB/s][w=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=131: Thu Jul 21 09:43:08 2022
  write: IOPS=49, BW=49.3MiB/s (51.7MB/s)(2958MiB/60007msec); 0 zone resets
    slat (usec): min=3273, max=23649, avg=20281.38, stdev=2331.03
    clat (usec): min=5, max=2622.0k, avg=2551059.28, stdev=316568.87
     lat (msec): min=21, max=2644, avg=2571.34, stdev=316.97
    clat percentiles (msec):
     |  1.00th=[  600],  5.00th=[ 2299], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2635], 90.00th=[ 2635], 95.00th=[ 2635],
     | 99.00th=[ 2635], 99.50th=[ 2635], 99.90th=[ 2635], 99.95th=[ 2635],
     | 99.99th=[ 2635]
   bw (  KiB/s): min=43008, max=51200, per=98.46%, avg=49699.31, stdev=1125.23, samples=116
   iops        : min=   42, max=   50, avg=48.53, stdev= 1.10, samples=116
  lat (usec)   : 10=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.41%, 750=0.41%
  lat (msec)   : 1000=0.41%, 2000=2.30%, >=2000=96.04%
  cpu          : usr=0.26%, sys=0.42%, ctx=8867, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,2958,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.3MiB/s (51.7MB/s), 49.3MiB/s-49.3MiB/s (51.7MB/s-51.7MB/s), io=2958MiB (3102MB), run=60007-60007msec
-------------------SIZE:32M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 32MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=11.2MiB/s][r=2856 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=134: Thu Jul 21 09:44:09 2022
  read: IOPS=2803, BW=10.0MiB/s (11.5MB/s)(657MiB/60001msec)
    slat (usec): min=234, max=12968, avg=354.47, stdev=128.45
    clat (usec): min=2, max=91529, avg=45284.08, stdev=3572.67
     lat (usec): min=364, max=92721, avg=45638.85, stdev=3592.80
    clat percentiles (usec):
     |  1.00th=[41157],  5.00th=[42206], 10.00th=[42206], 20.00th=[43254],
     | 30.00th=[43779], 40.00th=[44303], 50.00th=[44827], 60.00th=[45351],
     | 70.00th=[45876], 80.00th=[46924], 90.00th=[47973], 95.00th=[50070],
     | 99.00th=[58983], 99.50th=[65799], 99.90th=[81265], 99.95th=[84411],
     | 99.99th=[89654]
   bw (  KiB/s): min= 9504, max=11856, per=100.00%, avg=11222.78, stdev=415.24, samples=119
   iops        : min= 2376, max= 2964, avg=2805.69, stdev=103.82, samples=119
  lat (usec)   : 4=0.01%, 500=0.01%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=95.25%
  lat (msec)   : 100=4.71%
  cpu          : usr=1.65%, sys=5.96%, ctx=168223, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=168203,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=10.0MiB/s (11.5MB/s), 10.0MiB/s-10.0MiB/s (11.5MB/s-11.5MB/s), io=657MiB (689MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=7004KiB/s][w=1751 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=137: Thu Jul 21 09:45:09 2022
  write: IOPS=1745, BW=6981KiB/s (7149kB/s)(409MiB/60001msec); 0 zone resets
    slat (usec): min=275, max=34433, avg=569.81, stdev=309.60
    clat (usec): min=2, max=134501, avg=72723.40, stdev=6096.94
     lat (usec): min=365, max=135239, avg=73293.60, stdev=6131.44
    clat percentiles (msec):
     |  1.00th=[   63],  5.00th=[   65], 10.00th=[   66], 20.00th=[   69],
     | 30.00th=[   70], 40.00th=[   71], 50.00th=[   72], 60.00th=[   74],
     | 70.00th=[   75], 80.00th=[   78], 90.00th=[   80], 95.00th=[   83],
     | 99.00th=[   91], 99.50th=[   97], 99.90th=[  114], 99.95th=[  123],
     | 99.99th=[  133]
   bw (  KiB/s): min= 5712, max= 8032, per=100.00%, avg=6981.37, stdev=406.60, samples=119
   iops        : min= 1428, max= 2008, avg=1745.34, stdev=101.66, samples=119
  lat (usec)   : 4=0.01%, 500=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=0.05%
  lat (msec)   : 100=99.50%, 250=0.42%
  cpu          : usr=1.42%, sys=7.45%, ctx=217735, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,104723,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=6981KiB/s (7149kB/s), 6981KiB/s-6981KiB/s (7149kB/s-7149kB/s), io=409MiB (429MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=47.0MiB/s][r=47 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=140: Thu Jul 21 09:46:10 2022
  read: IOPS=50, BW=50.1MiB/s (52.5MB/s)(3006MiB/60020msec)
    slat (usec): min=1871, max=26197, avg=19961.93, stdev=3084.29
    clat (usec): min=3, max=2607.2k, avg=2524354.75, stdev=335891.85
     lat (msec): min=21, max=2627, avg=2544.32, stdev=336.97
    clat percentiles (msec):
     |  1.00th=[  617],  5.00th=[ 2005], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2601], 99.50th=[ 2601], 99.90th=[ 2601], 99.95th=[ 2601],
     | 99.99th=[ 2601]
   bw (  KiB/s): min= 8192, max=51200, per=96.92%, avg=49707.39, stdev=3986.55, samples=118
   iops        : min=    8, max=   50, avg=48.54, stdev= 3.89, samples=118
  lat (usec)   : 4=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.40%, 750=0.40%
  lat (msec)   : 1000=0.40%, 2000=3.33%, >=2000=95.04%
  cpu          : usr=0.03%, sys=0.26%, ctx=3009, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=3006,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=50.1MiB/s (52.5MB/s), 50.1MiB/s-50.1MiB/s (52.5MB/s-52.5MB/s), io=3006MiB (3152MB), run=60020-60020msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.0MiB/s][w=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=143: Thu Jul 21 09:47:11 2022
  write: IOPS=49, BW=49.4MiB/s (51.8MB/s)(2964MiB/60018msec); 0 zone resets
    slat (usec): min=3407, max=76324, avg=20243.53, stdev=2693.76
    clat (usec): min=4, max=2669.8k, avg=2546413.60, stdev=316060.63
     lat (msec): min=20, max=2690, avg=2566.66, stdev=316.46
    clat percentiles (msec):
     |  1.00th=[  592],  5.00th=[ 2299], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2601], 99.50th=[ 2601], 99.90th=[ 2635], 99.95th=[ 2668],
     | 99.99th=[ 2668]
   bw (  KiB/s): min=43008, max=51200, per=98.45%, avg=49787.59, stdev=1158.96, samples=116
   iops        : min=   42, max=   50, avg=48.62, stdev= 1.13, samples=116
  lat (usec)   : 10=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.40%, 750=0.40%
  lat (msec)   : 1000=0.40%, 2000=2.29%, >=2000=96.05%
  cpu          : usr=0.24%, sys=0.47%, ctx=8887, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,2964,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.4MiB/s (51.8MB/s), 49.4MiB/s-49.4MiB/s (51.8MB/s-51.8MB/s), io=2964MiB (3108MB), run=60018-60018msec
-------------------SIZE:64M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 64MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=10.5MiB/s][r=2682 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=146: Thu Jul 21 09:48:13 2022
  read: IOPS=2706, BW=10.6MiB/s (11.1MB/s)(634MiB/60001msec)
    slat (usec): min=234, max=16070, avg=367.23, stdev=150.34
    clat (usec): min=3, max=168875, avg=46902.57, stdev=5410.71
     lat (usec): min=331, max=169960, avg=47270.09, stdev=5446.01
    clat percentiles (msec):
     |  1.00th=[   43],  5.00th=[   44], 10.00th=[   44], 20.00th=[   45],
     | 30.00th=[   46], 40.00th=[   46], 50.00th=[   47], 60.00th=[   47],
     | 70.00th=[   48], 80.00th=[   49], 90.00th=[   50], 95.00th=[   52],
     | 99.00th=[   58], 99.50th=[   83], 99.90th=[  140], 99.95th=[  155],
     | 99.99th=[  167]
   bw (  KiB/s): min= 7984, max=11680, per=100.00%, avg=10832.13, stdev=531.16, samples=119
   iops        : min= 1996, max= 2920, avg=2708.03, stdev=132.79, samples=119
  lat (usec)   : 4=0.01%, 500=0.01%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=91.79%
  lat (msec)   : 100=8.03%, 250=0.15%
  cpu          : usr=1.48%, sys=5.64%, ctx=162410, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=162392,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=10.6MiB/s (11.1MB/s), 10.6MiB/s-10.6MiB/s (11.1MB/s-11.1MB/s), io=634MiB (665MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=7408KiB/s][w=1852 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=149: Thu Jul 21 09:49:14 2022
  write: IOPS=1730, BW=6922KiB/s (7088kB/s)(406MiB/60001msec); 0 zone resets
    slat (usec): min=275, max=6488, avg=574.84, stdev=244.95
    clat (usec): min=2, max=99605, avg=73333.75, stdev=6164.91
     lat (usec): min=332, max=99950, avg=73908.93, stdev=6203.00
    clat percentiles (usec):
     |  1.00th=[61604],  5.00th=[63701], 10.00th=[65274], 20.00th=[68682],
     | 30.00th=[69731], 40.00th=[71828], 50.00th=[72877], 60.00th=[74974],
     | 70.00th=[76022], 80.00th=[78119], 90.00th=[81265], 95.00th=[83362],
     | 99.00th=[88605], 99.50th=[90702], 99.90th=[96994], 99.95th=[99091],
     | 99.99th=[99091]
   bw (  KiB/s): min= 5277, max= 7952, per=100.00%, avg=6923.20, stdev=464.37, samples=119
   iops        : min= 1319, max= 1988, avg=1730.80, stdev=116.10, samples=119
  lat (usec)   : 4=0.01%, 500=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.02%, 50=0.05%
  lat (msec)   : 100=99.91%
  cpu          : usr=1.41%, sys=7.33%, ctx=215670, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,103830,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=6922KiB/s (7088kB/s), 6922KiB/s-6922KiB/s (7088kB/s-7088kB/s), io=406MiB (425MB), run=60001-60001msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=49.0MiB/s][r=49 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=152: Thu Jul 21 09:50:15 2022
  read: IOPS=50, BW=50.3MiB/s (52.8MB/s)(3021MiB/60018msec)
    slat (usec): min=1901, max=31587, avg=19862.36, stdev=3331.43
    clat (usec): min=7, max=2610.1k, avg=2514672.33, stdev=356391.55
     lat (msec): min=20, max=2630, avg=2534.54, stdev=357.83
    clat percentiles (msec):
     |  1.00th=[  617],  5.00th=[ 1854], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2601], 99.50th=[ 2601], 99.90th=[ 2601], 99.95th=[ 2601],
     | 99.99th=[ 2601]
   bw (  KiB/s): min=38912, max=51200, per=96.95%, avg=49967.73, stdev=1445.42, samples=118
   iops        : min=   38, max=   50, avg=48.80, stdev= 1.41, samples=118
  lat (usec)   : 10=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.26%, 500=0.40%, 750=0.40%
  lat (msec)   : 1000=0.86%, 2000=3.44%, >=2000=94.47%
  cpu          : usr=0.04%, sys=0.29%, ctx=3023, majf=0, minf=586
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=3021,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=50.3MiB/s (52.8MB/s), 50.3MiB/s-50.3MiB/s (52.8MB/s-52.8MB/s), io=3021MiB (3168MB), run=60018-60018msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.0MiB/s][w=48 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=155: Thu Jul 21 09:51:16 2022
  write: IOPS=49, BW=49.4MiB/s (51.8MB/s)(2964MiB/60008msec); 0 zone resets
    slat (usec): min=3565, max=70880, avg=20240.54, stdev=2558.08
    clat (usec): min=3, max=2661.9k, avg=2546100.58, stdev=316058.91
     lat (msec): min=21, max=2682, avg=2566.34, stdev=316.46
    clat percentiles (msec):
     |  1.00th=[  592],  5.00th=[ 2299], 10.00th=[ 2601], 20.00th=[ 2601],
     | 30.00th=[ 2601], 40.00th=[ 2601], 50.00th=[ 2601], 60.00th=[ 2601],
     | 70.00th=[ 2601], 80.00th=[ 2601], 90.00th=[ 2601], 95.00th=[ 2601],
     | 99.00th=[ 2635], 99.50th=[ 2635], 99.90th=[ 2635], 99.95th=[ 2635],
     | 99.99th=[ 2668]
   bw (  KiB/s): min=43008, max=51200, per=98.47%, avg=49805.24, stdev=1164.78, samples=116
   iops        : min=   42, max=   50, avg=48.64, stdev= 1.14, samples=116
  lat (usec)   : 4=0.03%
  lat (msec)   : 50=0.07%, 100=0.07%, 250=0.27%, 500=0.40%, 750=0.40%
  lat (msec)   : 1000=0.40%, 2000=2.29%, >=2000=96.05%
  cpu          : usr=0.25%, sys=0.47%, ctx=8888, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.3%, 16=0.5%, 32=1.1%, >=64=97.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,2964,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.4MiB/s (51.8MB/s), 49.4MiB/s-49.4MiB/s (51.8MB/s-51.8MB/s), io=2964MiB (3108MB), run=60008-60008msec
```

### FS

```
-------------------SIZE:4M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=160: Thu Jul 21 09:53:53 2022
  read: IOPS=25.4k, BW=99.2MiB/s (104MB/s)(5951MiB/60005msec)
    slat (nsec): min=1332, max=360355, avg=6348.60, stdev=7466.75
    clat (usec): min=1147, max=74458, avg=5033.96, stdev=910.66
     lat (usec): min=1150, max=74462, avg=5040.52, stdev=910.76
    clat percentiles (usec):
     |  1.00th=[ 3359],  5.00th=[ 3916], 10.00th=[ 4228], 20.00th=[ 4555],
     | 30.00th=[ 4752], 40.00th=[ 4948], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5407], 90.00th=[ 5735], 95.00th=[ 5997],
     | 99.00th=[ 7242], 99.50th=[ 7963], 99.90th=[10028], 99.95th=[11207],
     | 99.99th=[14091]
   bw (  KiB/s): min=96520, max=131504, per=100.00%, avg=101649.00, stdev=4575.73, samples=119
   iops        : min=24130, max=32876, avg=25412.24, stdev=1143.93, samples=119
  lat (msec)   : 2=0.01%, 4=5.92%, 10=93.97%, 20=0.09%, 100=0.01%
  cpu          : usr=5.32%, sys=18.11%, ctx=260391, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1523403,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.2MiB/s (104MB/s), 99.2MiB/s-99.2MiB/s (104MB/s-104MB/s), io=5951MiB (6240MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.8MiB/s][w=12.5k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=163: Thu Jul 21 09:54:54 2022
  write: IOPS=12.6k, BW=49.3MiB/s (51.7MB/s)(2960MiB/60013msec); 0 zone resets
    slat (nsec): min=1492, max=286468, avg=8866.52, stdev=8070.22
    clat (usec): min=4226, max=40657, avg=10126.10, stdev=1787.17
     lat (usec): min=4241, max=40659, avg=10135.19, stdev=1787.13
    clat percentiles (usec):
     |  1.00th=[ 7832],  5.00th=[ 8291], 10.00th=[ 8586], 20.00th=[ 8848],
     | 30.00th=[ 9110], 40.00th=[ 9372], 50.00th=[ 9765], 60.00th=[10028],
     | 70.00th=[10421], 80.00th=[11076], 90.00th=[12125], 95.00th=[13304],
     | 99.00th=[16450], 99.50th=[18220], 99.90th=[26870], 99.95th=[29492],
     | 99.99th=[32113]
   bw (  KiB/s): min=43696, max=55304, per=100.00%, avg=50573.28, stdev=2832.82, samples=119
   iops        : min=10924, max=13826, avg=12643.32, stdev=708.20, samples=119
  lat (msec)   : 10=58.39%, 20=41.35%, 50=0.27%
  cpu          : usr=4.04%, sys=13.43%, ctx=286955, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,757786,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.3MiB/s (51.7MB/s), 49.3MiB/s-49.3MiB/s (51.7MB/s-51.7MB/s), io=2960MiB (3104MB), run=60013-60013msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=207MiB/s][r=206 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=166: Thu Jul 21 09:55:55 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60457msec)
    slat (usec): min=40, max=450, avg=74.99, stdev=29.54
    clat (msec): min=24, max=972, avg=536.98, stdev=115.81
     lat (msec): min=24, max=972, avg=537.06, stdev=115.80
    clat percentiles (msec):
     |  1.00th=[  133],  5.00th=[  351], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  542], 40.00th=[  558], 50.00th=[  567], 60.00th=[  592],
     | 70.00th=[  609], 80.00th=[  617], 90.00th=[  651], 95.00th=[  659],
     | 99.00th=[  726], 99.50th=[  776], 99.90th=[  961], 99.95th=[  969],
     | 99.99th=[  969]
   bw (  KiB/s): min=137216, max=407703, per=99.46%, avg=242672.19, stdev=56428.20, samples=120
   iops        : min=  134, max=  398, avg=236.98, stdev=55.10, samples=120
  lat (msec)   : 50=0.27%, 100=0.35%, 250=0.76%, 500=27.55%, 750=70.37%
  lat (msec)   : 1000=0.70%
  cpu          : usr=0.12%, sys=2.16%, ctx=14406, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14405,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60457-60457msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=169: Thu Jul 21 09:56:57 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60538msec); 0 zone resets
    slat (usec): min=57, max=422, avg=102.86, stdev=25.49
    clat (msec): min=16, max=1073, avg=536.41, stdev=42.48
     lat (msec): min=16, max=1073, avg=536.52, stdev=42.48
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  531],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  567], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1036],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=155648, max=256000, per=99.81%, avg=243793.12, stdev=9427.07, samples=120
   iops        : min=  152, max=  250, avg=238.07, stdev= 9.20, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.09%, 250=0.26%, 500=0.44%
  lat (msec)   : 750=98.61%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.87%, sys=2.13%, ctx=14440, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14440,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60538-60538msec
-------------------SIZE:8M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=172: Thu Jul 21 09:57:58 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60007msec)
    slat (nsec): min=1342, max=342673, avg=6725.28, stdev=8008.82
    clat (usec): min=919, max=36294, avg=5028.19, stdev=1179.14
     lat (usec): min=922, max=36296, avg=5035.11, stdev=1179.20
    clat percentiles (usec):
     |  1.00th=[ 2835],  5.00th=[ 3326], 10.00th=[ 3687], 20.00th=[ 4293],
     | 30.00th=[ 4686], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5538], 90.00th=[ 5997], 95.00th=[ 6915],
     | 99.00th=[ 8979], 99.50th=[10028], 99.90th=[13566], 99.95th=[16450],
     | 99.99th=[29230]
   bw (  KiB/s): min=96992, max=126816, per=100.00%, avg=101749.57, stdev=5720.44, samples=119
   iops        : min=24248, max=31704, avg=25437.39, stdev=1430.10, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.02%, 4=15.01%, 10=84.46%, 20=0.47%, 50=0.03%
  cpu          : usr=5.56%, sys=18.85%, ctx=283394, majf=0, minf=138
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1525080,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6247MB), run=60007-60007msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=45.0MiB/s][w=11.8k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=175: Thu Jul 21 09:58:59 2022
  write: IOPS=11.8k, BW=46.1MiB/s (48.4MB/s)(2769MiB/60013msec); 0 zone resets
    slat (nsec): min=1492, max=547877, avg=8944.31, stdev=8065.41
    clat (usec): min=4775, max=43647, avg=10824.17, stdev=2309.11
     lat (usec): min=4778, max=43653, avg=10833.34, stdev=2309.07
    clat percentiles (usec):
     |  1.00th=[ 7898],  5.00th=[ 8356], 10.00th=[ 8586], 20.00th=[ 9110],
     | 30.00th=[ 9372], 40.00th=[ 9896], 50.00th=[10290], 60.00th=[10814],
     | 70.00th=[11469], 80.00th=[12125], 90.00th=[13435], 95.00th=[15008],
     | 99.00th=[19268], 99.50th=[21365], 99.90th=[27132], 99.95th=[29492],
     | 99.99th=[33817]
   bw (  KiB/s): min=44136, max=48992, per=100.00%, avg=47310.06, stdev=923.26, samples=119
   iops        : min=11034, max=12248, avg=11827.51, stdev=230.82, samples=119
  lat (msec)   : 10=43.07%, 20=56.14%, 50=0.79%
  cpu          : usr=4.06%, sys=12.53%, ctx=267775, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,708931,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=46.1MiB/s (48.4MB/s), 46.1MiB/s-46.1MiB/s (48.4MB/s-48.4MB/s), io=2769MiB (2904MB), run=60013-60013msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=222MiB/s][r=221 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=178: Thu Jul 21 10:00:00 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60517msec)
    slat (usec): min=40, max=475, avg=73.58, stdev=25.09
    clat (msec): min=19, max=1092, avg=537.57, stdev=118.93
     lat (msec): min=19, max=1093, avg=537.65, stdev=118.93
    clat percentiles (msec):
     |  1.00th=[  161],  5.00th=[  351], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  477], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  726], 99.50th=[  760], 99.90th=[ 1083], 99.95th=[ 1083],
     | 99.99th=[ 1099]
   bw (  KiB/s): min=137216, max=377679, per=99.59%, avg=242729.19, stdev=59523.99, samples=120
   iops        : min=  134, max=  368, avg=237.03, stdev=58.11, samples=120
  lat (msec)   : 20=0.03%, 50=0.22%, 100=0.50%, 250=0.44%, 500=29.96%
  lat (msec)   : 750=68.22%, 1000=0.32%, 2000=0.31%
  cpu          : usr=0.12%, sys=2.14%, ctx=14411, majf=0, minf=584
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14404,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60517-60517msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=181: Thu Jul 21 10:01:01 2022
  write: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60537msec); 0 zone resets
    slat (usec): min=56, max=552, avg=105.88, stdev=28.17
    clat (msec): min=14, max=1072, avg=536.48, stdev=42.22
     lat (msec): min=14, max=1072, avg=536.59, stdev=42.22
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  518], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  558], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1036],
     | 99.99th=[ 1062]
   bw (  KiB/s): min=157696, max=258048, per=99.81%, avg=243762.37, stdev=9187.05, samples=120
   iops        : min=  154, max=  252, avg=238.04, stdev= 8.97, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.08%, 250=0.27%, 500=0.44%
  lat (msec)   : 750=98.62%, 1000=0.40%, 2000=0.12%
  cpu          : usr=0.91%, sys=2.21%, ctx=14453, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14438,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60537-60537msec
-------------------SIZE:16M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=97.8MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=184: Thu Jul 21 10:02:02 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1312, max=1034.5k, avg=6425.87, stdev=7641.21
    clat (usec): min=970, max=55649, avg=5028.66, stdev=1118.81
     lat (usec): min=980, max=55651, avg=5035.28, stdev=1118.85
    clat percentiles (usec):
     |  1.00th=[ 3228],  5.00th=[ 3720], 10.00th=[ 4047], 20.00th=[ 4424],
     | 30.00th=[ 4686], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5473], 90.00th=[ 5866], 95.00th=[ 6325],
     | 99.00th=[ 7963], 99.50th=[ 8717], 99.90th=[11076], 99.95th=[12780],
     | 99.99th=[51643]
   bw (  KiB/s): min=94736, max=121240, per=100.00%, avg=101760.63, stdev=4583.10, samples=119
   iops        : min=23684, max=30310, avg=25440.15, stdev=1145.77, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.01%, 4=9.29%, 10=90.52%, 20=0.16%, 50=0.01%
  lat (msec)   : 100=0.02%
  cpu          : usr=5.33%, sys=18.20%, ctx=267346, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1525005,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=47.9MiB/s][w=12.3k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=187: Thu Jul 21 10:03:03 2022
  write: IOPS=12.3k, BW=47.9MiB/s (50.3MB/s)(2876MiB/60010msec); 0 zone resets
    slat (nsec): min=1462, max=266730, avg=8873.11, stdev=8066.63
    clat (usec): min=4480, max=46358, avg=10421.76, stdev=1692.64
     lat (usec): min=4487, max=46368, avg=10430.87, stdev=1692.57
    clat percentiles (usec):
     |  1.00th=[ 8094],  5.00th=[ 8586], 10.00th=[ 8979], 20.00th=[ 9372],
     | 30.00th=[ 9634], 40.00th=[ 9896], 50.00th=[10159], 60.00th=[10421],
     | 70.00th=[10814], 80.00th=[11207], 90.00th=[11994], 95.00th=[13042],
     | 99.00th=[16450], 99.50th=[18744], 99.90th=[26608], 99.95th=[29492],
     | 99.99th=[38536]
   bw (  KiB/s): min=44280, max=53400, per=100.00%, avg=49119.06, stdev=1951.84, samples=119
   iops        : min=11070, max=13350, avg=12279.76, stdev=487.96, samples=119
  lat (msec)   : 10=44.86%, 20=54.78%, 50=0.36%
  cpu          : usr=4.12%, sys=12.83%, ctx=271261, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,736273,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=47.9MiB/s (50.3MB/s), 47.9MiB/s-47.9MiB/s (50.3MB/s-50.3MB/s), io=2876MiB (3016MB), run=60010-60010msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=207MiB/s][r=206 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=190: Thu Jul 21 10:04:04 2022
  read: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60353msec)
    slat (usec): min=40, max=407, avg=75.39, stdev=28.12
    clat (msec): min=19, max=1011, avg=536.33, stdev=118.91
     lat (msec): min=20, max=1011, avg=536.41, stdev=118.90
    clat percentiles (msec):
     |  1.00th=[  142],  5.00th=[  355], 10.00th=[  372], 20.00th=[  401],
     | 30.00th=[  451], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  676],
     | 99.00th=[  718], 99.50th=[  726], 99.90th=[  995], 99.95th=[ 1003],
     | 99.99th=[ 1011]
   bw (  KiB/s): min=49152, max=380252, per=99.31%, avg=242614.10, stdev=65863.62, samples=120
   iops        : min=   48, max=  371, avg=236.93, stdev=64.31, samples=120
  lat (msec)   : 20=0.01%, 50=0.12%, 100=0.55%, 250=0.52%, 500=31.53%
  lat (msec)   : 750=67.11%, 1000=0.08%, 2000=0.08%
  cpu          : usr=0.14%, sys=2.17%, ctx=14408, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14398,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60353-60353msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=193: Thu Jul 21 10:05:06 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60540msec); 0 zone resets
    slat (usec): min=58, max=532, avg=104.92, stdev=28.51
    clat (msec): min=19, max=1073, avg=536.42, stdev=42.37
     lat (msec): min=19, max=1073, avg=536.53, stdev=42.37
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  558], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=157696, max=258048, per=99.82%, avg=243793.12, stdev=9173.14, samples=120
   iops        : min=  154, max=  252, avg=238.08, stdev= 8.96, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.08%, 250=0.26%, 500=0.45%
  lat (msec)   : 750=98.61%, 1000=0.40%, 2000=0.12%
  cpu          : usr=0.86%, sys=2.20%, ctx=14443, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14440,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60540-60540msec
-------------------SIZE:32M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=196: Thu Jul 21 10:06:07 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1322, max=1377.7k, avg=6630.77, stdev=8077.99
    clat (usec): min=1165, max=25203, avg=5028.15, stdev=713.41
     lat (usec): min=1170, max=25207, avg=5034.97, stdev=713.54
    clat percentiles (usec):
     |  1.00th=[ 3294],  5.00th=[ 3884], 10.00th=[ 4228], 20.00th=[ 4555],
     | 30.00th=[ 4752], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5473], 90.00th=[ 5735], 95.00th=[ 6063],
     | 99.00th=[ 6980], 99.50th=[ 7504], 99.90th=[10028], 99.95th=[11731],
     | 99.99th=[14484]
   bw (  KiB/s): min=97112, max=128351, per=100.00%, avg=101711.12, stdev=6131.33, samples=119
   iops        : min=24278, max=32087, avg=25427.77, stdev=1532.80, samples=119
  lat (msec)   : 2=0.01%, 4=6.45%, 10=93.44%, 20=0.10%, 50=0.01%
  cpu          : usr=5.31%, sys=19.00%, ctx=282215, majf=0, minf=136
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1525067,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6247MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.6MiB/s][w=12.4k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=199: Thu Jul 21 10:07:08 2022
  write: IOPS=12.7k, BW=49.6MiB/s (51.0MB/s)(2974MiB/60014msec); 0 zone resets
    slat (nsec): min=1483, max=2068.1k, avg=9000.57, stdev=8575.65
    clat (usec): min=2867, max=44945, avg=10078.14, stdev=1413.98
     lat (usec): min=2892, max=44950, avg=10087.36, stdev=1413.96
    clat percentiles (usec):
     |  1.00th=[ 7963],  5.00th=[ 8455], 10.00th=[ 8717], 20.00th=[ 9110],
     | 30.00th=[ 9503], 40.00th=[ 9765], 50.00th=[ 9896], 60.00th=[10159],
     | 70.00th=[10421], 80.00th=[10683], 90.00th=[11338], 95.00th=[11994],
     | 99.00th=[14877], 99.50th=[16712], 99.90th=[24773], 99.95th=[29230],
     | 99.99th=[34866]
   bw (  KiB/s): min=43376, max=56640, per=100.00%, avg=50812.88, stdev=2345.16, samples=119
   iops        : min=10844, max=14160, avg=12703.22, stdev=586.29, samples=119
  lat (msec)   : 4=0.01%, 10=52.66%, 20=47.15%, 50=0.19%
  cpu          : usr=4.33%, sys=14.12%, ctx=341496, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,761392,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.6MiB/s (51.0MB/s), 49.6MiB/s-49.6MiB/s (51.0MB/s-51.0MB/s), io=2974MiB (3119MB), run=60014-60014msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=222MiB/s][r=221 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=202: Thu Jul 21 10:08:09 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60403msec)
    slat (usec): min=41, max=566, avg=77.37, stdev=30.01
    clat (msec): min=22, max=970, avg=536.66, stdev=115.07
     lat (msec): min=22, max=970, avg=536.74, stdev=115.06
    clat percentiles (msec):
     |  1.00th=[  146],  5.00th=[  355], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  464], 40.00th=[  558], 50.00th=[  575], 60.00th=[  592],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  701], 99.50th=[  718], 99.90th=[  953], 99.95th=[  961],
     | 99.99th=[  969]
   bw (  KiB/s): min=145408, max=376098, per=99.40%, avg=242681.88, stdev=57570.72, samples=120
   iops        : min=  142, max=  367, avg=236.99, stdev=56.22, samples=120
  lat (msec)   : 50=0.09%, 100=0.44%, 250=0.62%, 500=29.14%, 750=69.38%
  lat (msec)   : 1000=0.32%
  cpu          : usr=0.14%, sys=2.22%, ctx=14415, majf=0, minf=584
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14401,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60403-60403msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=205: Thu Jul 21 10:09:10 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60548msec); 0 zone resets
    slat (usec): min=56, max=496, avg=109.10, stdev=27.26
    clat (msec): min=16, max=1073, avg=536.45, stdev=42.90
     lat (msec): min=16, max=1073, avg=536.56, stdev=42.91
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  531],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  567], 99.50th=[  776], 99.90th=[ 1020], 99.95th=[ 1053],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=155648, max=256000, per=99.83%, avg=243810.18, stdev=9521.77, samples=120
   iops        : min=  152, max=  250, avg=238.09, stdev= 9.30, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.08%, 250=0.27%, 500=0.51%
  lat (msec)   : 750=98.52%, 1000=0.41%, 2000=0.14%
  cpu          : usr=0.98%, sys=2.23%, ctx=14441, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14441,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60548-60548msec
-------------------SIZE:64M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=99.2MiB/s][r=25.4k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=208: Thu Jul 21 10:10:11 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1312, max=615725, avg=6483.06, stdev=7612.49
    clat (usec): min=1385, max=24597, avg=5028.65, stdev=739.73
     lat (usec): min=1389, max=24599, avg=5035.32, stdev=739.86
    clat percentiles (usec):
     |  1.00th=[ 3425],  5.00th=[ 3916], 10.00th=[ 4178], 20.00th=[ 4490],
     | 30.00th=[ 4686], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5342], 80.00th=[ 5538], 90.00th=[ 5866], 95.00th=[ 6128],
     | 99.00th=[ 7046], 99.50th=[ 7570], 99.90th=[10290], 99.95th=[12256],
     | 99.99th=[14746]
   bw (  KiB/s): min=88856, max=122944, per=100.00%, avg=101750.89, stdev=5653.70, samples=119
   iops        : min=22214, max=30736, avg=25437.72, stdev=1413.43, samples=119
  lat (msec)   : 2=0.01%, 4=6.41%, 10=93.47%, 20=0.11%, 50=0.01%
  cpu          : usr=5.36%, sys=18.26%, ctx=259235, majf=0, minf=138
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1524986,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=48.9MiB/s][w=12.5k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=211: Thu Jul 21 10:11:12 2022
  write: IOPS=12.7k, BW=49.5MiB/s (51.9MB/s)(2972MiB/60011msec); 0 zone resets
    slat (nsec): min=1502, max=1363.1k, avg=8808.94, stdev=8030.32
    clat (usec): min=3185, max=38988, avg=10084.55, stdev=1336.68
     lat (usec): min=3188, max=39015, avg=10093.59, stdev=1336.64
    clat percentiles (usec):
     |  1.00th=[ 8029],  5.00th=[ 8455], 10.00th=[ 8717], 20.00th=[ 9110],
     | 30.00th=[ 9372], 40.00th=[ 9634], 50.00th=[ 9896], 60.00th=[10159],
     | 70.00th=[10421], 80.00th=[10814], 90.00th=[11469], 95.00th=[12125],
     | 99.00th=[14353], 99.50th=[16057], 99.90th=[20841], 99.95th=[27657],
     | 99.99th=[32900]
   bw (  KiB/s): min=44112, max=55904, per=100.00%, avg=50774.62, stdev=2441.39, samples=119
   iops        : min=11028, max=13976, avg=12693.66, stdev=610.35, samples=119
  lat (msec)   : 4=0.01%, 10=52.93%, 20=46.95%, 50=0.12%
  cpu          : usr=4.25%, sys=13.59%, ctx=313151, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,760874,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=49.5MiB/s (51.9MB/s), 49.5MiB/s-49.5MiB/s (51.9MB/s-51.9MB/s), io=2972MiB (3117MB), run=60011-60011msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=276MiB/s][r=275 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=214: Thu Jul 21 10:12:14 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60511msec)
    slat (usec): min=40, max=524, avg=75.39, stdev=26.27
    clat (msec): min=23, max=912, avg=536.81, stdev=110.77
     lat (msec): min=23, max=912, avg=536.89, stdev=110.77
    clat percentiles (msec):
     |  1.00th=[  146],  5.00th=[  355], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  550], 40.00th=[  558], 50.00th=[  567], 60.00th=[  584],
     | 70.00th=[  600], 80.00th=[  617], 90.00th=[  642], 95.00th=[  659],
     | 99.00th=[  684], 99.50th=[  726], 99.90th=[  894], 99.95th=[  902],
     | 99.99th=[  911]
   bw (  KiB/s): min=135168, max=369777, per=99.59%, avg=243072.94, stdev=59274.78, samples=120
   iops        : min=  132, max=  361, avg=237.37, stdev=57.88, samples=120
  lat (msec)   : 50=0.03%, 100=0.38%, 250=0.75%, 500=25.97%, 750=72.45%
  lat (msec)   : 1000=0.43%
  cpu          : usr=0.16%, sys=2.15%, ctx=14436, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14423,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60511-60511msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=217: Thu Jul 21 10:13:15 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60533msec); 0 zone resets
    slat (usec): min=58, max=690, avg=104.31, stdev=24.96
    clat (msec): min=18, max=1071, avg=536.44, stdev=42.45
     lat (msec): min=18, max=1071, avg=536.55, stdev=42.46
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  558], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=151552, max=256000, per=99.80%, avg=243758.98, stdev=9732.67, samples=120
   iops        : min=  148, max=  250, avg=238.04, stdev= 9.50, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.09%, 250=0.26%, 500=0.44%
  lat (msec)   : 750=98.60%, 1000=0.42%, 2000=0.12%
  cpu          : usr=0.89%, sys=2.15%, ctx=14445, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14438,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60533-60533msec
```

### 块设备

```
-------------------SIZE:4M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=15.8MiB/s][r=4037 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=82: Thu Jul 21 09:06:59 2022
  read: IOPS=4175, BW=16.3MiB/s (17.1MB/s)(979MiB/60051msec)
    slat (nsec): min=1352, max=208652, avg=5316.82, stdev=3079.48
    clat (usec): min=296, max=244259, avg=30649.90, stdev=20896.45
     lat (usec): min=299, max=244266, avg=30655.39, stdev=20896.55
    clat percentiles (usec):
     |  1.00th=[  1045],  5.00th=[  2507], 10.00th=[  4883], 20.00th=[ 10814],
     | 30.00th=[ 16909], 40.00th=[ 22938], 50.00th=[ 29492], 60.00th=[ 34341],
     | 70.00th=[ 40109], 80.00th=[ 47973], 90.00th=[ 58459], 95.00th=[ 65274],
     | 99.00th=[ 85459], 99.50th=[107480], 99.90th=[149947], 99.95th=[164627],
     | 99.99th=[208667]
   bw (  KiB/s): min=15104, max=58486, per=99.57%, avg=16627.48, stdev=3894.19, samples=119
   iops        : min= 3776, max=14621, avg=4156.87, stdev=973.50, samples=119
  lat (usec)   : 500=0.05%, 750=0.34%, 1000=0.49%
  lat (msec)   : 2=2.68%, 4=4.88%, 10=10.17%, 20=16.55%, 50=47.20%
  lat (msec)   : 100=17.00%, 250=0.64%
  cpu          : usr=2.14%, sys=4.37%, ctx=170887, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=250725,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=16.3MiB/s (17.1MB/s), 16.3MiB/s-16.3MiB/s (17.1MB/s-17.1MB/s), io=979MiB (1027MB), run=60051-60051msec

Disk stats (read/write):
  sdb: ios=183469/3, merge=63666/1, ticks=5794556/75, in_queue=5699808, util=99.97%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=14.0MiB/s][w=3587 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=85: Thu Jul 21 09:08:00 2022
  write: IOPS=3397, BW=13.3MiB/s (13.9MB/s)(797MiB/60042msec); 0 zone resets
    slat (nsec): min=1603, max=59876k, avg=75319.90, stdev=1271137.40
    clat (usec): min=938, max=155490, avg=37596.19, stdev=22091.95
     lat (usec): min=941, max=155495, avg=37671.65, stdev=22100.46
    clat percentiles (msec):
     |  1.00th=[    3],  5.00th=[    5], 10.00th=[   10], 20.00th=[   19],
     | 30.00th=[   25], 40.00th=[   31], 50.00th=[   36], 60.00th=[   41],
     | 70.00th=[   46], 80.00th=[   55], 90.00th=[   67], 95.00th=[   82],
     | 99.00th=[  101], 99.50th=[  107], 99.90th=[  120], 99.95th=[  124],
     | 99.99th=[  138]
   bw (  KiB/s): min=11800, max=30040, per=99.82%, avg=13565.24, stdev=1708.79, samples=119
   iops        : min= 2950, max= 7510, avg=3391.31, stdev=427.20, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.15%, 4=3.38%, 10=6.55%, 20=12.22%, 50=52.61%
  lat (msec)   : 100=24.12%, 250=0.97%
  cpu          : usr=0.48%, sys=2.01%, ctx=4584, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,204001,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=13.3MiB/s (13.9MB/s), 13.3MiB/s-13.3MiB/s (13.9MB/s-13.9MB/s), io=797MiB (836MB), run=60042-60042msec

Disk stats (read/write):
  sdb: ios=0/181156, merge=0/30354, ticks=0/2556302, in_queue=2463129, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=88: Thu Jul 21 09:09:06 2022
  read: IOPS=24, BW=24.1MiB/s (25.3MB/s)(1582MiB/65545msec)
    slat (usec): min=12, max=360, avg=47.16, stdev=32.51
    clat (msec): min=12, max=11523, avg=5299.13, stdev=1825.36
     lat (msec): min=12, max=11523, avg=5299.18, stdev=1825.35
    clat percentiles (msec):
     |  1.00th=[   49],  5.00th=[ 1351], 10.00th=[ 3574], 20.00th=[ 4279],
     | 30.00th=[ 4732], 40.00th=[ 5067], 50.00th=[ 5403], 60.00th=[ 5738],
     | 70.00th=[ 6074], 80.00th=[ 6477], 90.00th=[ 7080], 95.00th=[ 7550],
     | 99.00th=[10671], 99.50th=[11073], 99.90th=[11476], 99.95th=[11476],
     | 99.99th=[11476]
   bw (  KiB/s): min=16384, max=99249, per=99.47%, avg=24583.88, stdev=7023.16, samples=120
   iops        : min=   16, max=   96, avg=24.00, stdev= 6.78, samples=120
  lat (msec)   : 20=0.32%, 50=0.76%, 100=2.09%, 250=0.25%, 500=0.44%
  lat (msec)   : 750=0.32%, 1000=0.38%, 2000=1.52%, >=2000=93.93%
  cpu          : usr=0.03%, sys=0.16%, ctx=1580, majf=0, minf=586
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.0%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1582,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=24.1MiB/s (25.3MB/s), 24.1MiB/s-24.1MiB/s (25.3MB/s-25.3MB/s), io=1582MiB (1659MB), run=65545-65545msec

Disk stats (read/write):
  sdb: ios=1580/3, merge=0/1, ticks=8026953/5154, in_queue=8031261, util=99.87%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=91: Thu Jul 21 09:10:11 2022
  write: IOPS=23, BW=23.6MiB/s (24.7MB/s)(1524MiB/64637msec); 0 zone resets
    slat (usec): min=26, max=386, avg=48.17, stdev=20.97
    clat (msec): min=3419, max=10757, avg=5428.42, stdev=1350.19
     lat (msec): min=3419, max=10757, avg=5428.46, stdev=1350.19
    clat percentiles (msec):
     |  1.00th=[ 3406],  5.00th=[ 3440], 10.00th=[ 4178], 20.00th=[ 4597],
     | 30.00th=[ 5403], 40.00th=[ 5403], 50.00th=[ 5403], 60.00th=[ 5470],
     | 70.00th=[ 5470], 80.00th=[ 5537], 90.00th=[ 5537], 95.00th=[ 9329],
     | 99.00th=[10000], 99.50th=[10000], 99.90th=[10805], 99.95th=[10805],
     | 99.99th=[10805]
   bw (  KiB/s): min=198656, max=262144, per=100.00%, avg=238250.67, stdev=27160.43, samples=12
   iops        : min=  194, max=  256, avg=232.67, stdev=26.52, samples=12
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.06%, sys=0.06%, ctx=75, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1524,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.6MiB/s (24.7MB/s), 23.6MiB/s-23.6MiB/s (24.7MB/s-24.7MB/s), io=1524MiB (1598MB), run=64637-64637msec

Disk stats (read/write):
  sdb: ios=0/1544, merge=0/13, ticks=0/4446800, in_queue=4446024, util=99.87%
-------------------SIZE:8M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=13.8MiB/s][r=3532 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=94: Thu Jul 21 09:11:12 2022
  read: IOPS=3751, BW=14.7MiB/s (15.4MB/s)(880MiB/60046msec)
    slat (nsec): min=1352, max=281797, avg=5574.56, stdev=3247.57
    clat (usec): min=285, max=334967, avg=34112.37, stdev=23323.77
     lat (usec): min=297, max=334974, avg=34118.14, stdev=23323.84
    clat percentiles (usec):
     |  1.00th=[  1139],  5.00th=[  2933], 10.00th=[  5932], 20.00th=[ 12780],
     | 30.00th=[ 19530], 40.00th=[ 26608], 50.00th=[ 32637], 60.00th=[ 38011],
     | 70.00th=[ 43779], 80.00th=[ 51119], 90.00th=[ 63701], 95.00th=[ 72877],
     | 99.00th=[ 95945], 99.50th=[126354], 99.90th=[189793], 99.95th=[219153],
     | 99.99th=[267387]
   bw (  KiB/s): min=13328, max=51495, per=99.56%, avg=14938.72, stdev=3523.42, samples=119
   iops        : min= 3332, max=12873, avg=3734.67, stdev=880.79, samples=119
  lat (usec)   : 500=0.03%, 750=0.23%, 1000=0.44%
  lat (msec)   : 2=2.25%, 4=4.15%, 10=8.76%, 20=14.80%, 50=47.92%
  lat (msec)   : 100=20.51%, 250=0.89%, 500=0.02%
  cpu          : usr=2.22%, sys=4.06%, ctx=173276, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=225256,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=14.7MiB/s (15.4MB/s), 14.7MiB/s-14.7MiB/s (15.4MB/s-15.4MB/s), io=880MiB (923MB), run=60046-60046msec

Disk stats (read/write):
  sdb: ios=185321/3, merge=38679/1, ticks=6476848/86, in_queue=6379147, util=99.97%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=12.0MiB/s][w=3327 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=97: Thu Jul 21 09:12:13 2022
  write: IOPS=3243, BW=12.7MiB/s (13.3MB/s)(761MiB/60019msec); 0 zone resets
    slat (nsec): min=1573, max=41102k, avg=40378.10, stdev=780276.32
    clat (usec): min=1146, max=160623, avg=39416.05, stdev=20948.80
     lat (usec): min=1149, max=160627, avg=39456.57, stdev=20943.74
    clat percentiles (msec):
     |  1.00th=[    3],  5.00th=[    8], 10.00th=[   15], 20.00th=[   22],
     | 30.00th=[   28], 40.00th=[   34], 50.00th=[   39], 60.00th=[   43],
     | 70.00th=[   47], 80.00th=[   55], 90.00th=[   66], 95.00th=[   82],
     | 99.00th=[  103], 99.50th=[  109], 99.90th=[  125], 99.95th=[  132],
     | 99.99th=[  146]
   bw (  KiB/s): min=11248, max=28942, per=99.79%, avg=12948.29, stdev=1625.60, samples=119
   iops        : min= 2812, max= 7235, avg=3237.07, stdev=406.36, samples=119
  lat (msec)   : 2=0.22%, 4=1.91%, 10=4.46%, 20=10.47%, 50=58.18%
  lat (msec)   : 100=23.54%, 250=1.23%
  cpu          : usr=0.51%, sys=1.78%, ctx=3589, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,194700,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=12.7MiB/s (13.3MB/s), 12.7MiB/s-12.7MiB/s (13.3MB/s-13.3MB/s), io=761MiB (797MB), run=60019-60019msec

Disk stats (read/write):
  sdb: ios=0/180975, merge=0/20493, ticks=0/2725783, in_queue=2632975, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=100: Thu Jul 21 09:13:20 2022
  read: IOPS=23, BW=23.8MiB/s (24.0MB/s)(1559MiB/65490msec)
    slat (usec): min=12, max=498, avg=53.48, stdev=39.40
    clat (msec): min=14, max=12459, avg=5372.72, stdev=2279.27
     lat (msec): min=14, max=12459, avg=5372.77, stdev=2279.26
    clat percentiles (msec):
     |  1.00th=[   42],  5.00th=[ 1485], 10.00th=[ 2366], 20.00th=[ 3440],
     | 30.00th=[ 4178], 40.00th=[ 4866], 50.00th=[ 5403], 60.00th=[ 6007],
     | 70.00th=[ 6611], 80.00th=[ 7349], 90.00th=[ 8356], 95.00th=[ 9060],
     | 99.00th=[10268], 99.50th=[10805], 99.90th=[12281], 99.95th=[12416],
     | 99.99th=[12416]
   bw (  KiB/s): min=14336, max=80344, per=99.43%, avg=24238.23, stdev=5380.24, samples=120
   iops        : min=   14, max=   78, avg=23.66, stdev= 5.22, samples=120
  lat (msec)   : 20=0.32%, 50=1.41%, 100=0.71%, 250=0.26%, 500=0.38%
  lat (msec)   : 750=0.38%, 1000=0.45%, 2000=3.21%, >=2000=92.88%
  cpu          : usr=0.04%, sys=0.16%, ctx=1559, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1559,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.8MiB/s (24.0MB/s), 23.8MiB/s-23.8MiB/s (24.0MB/s-24.0MB/s), io=1559MiB (1635MB), run=65490-65490msec

Disk stats (read/write):
  sdb: ios=1558/3, merge=0/1, ticks=8024739/5427, in_queue=8029318, util=99.83%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                       
Fio: (groupid=0, jobs=1): err= 0: pid=103: Thu Jul 21 09:14:21 2022
  write: IOPS=23, BW=23.6MiB/s (24.8MB/s)(1418MiB/60026msec); 0 zone resets
    slat (usec): min=23, max=554577, avg=811.84, stdev=20340.96
    clat (msec): min=3485, max=10005, avg=5417.21, stdev=1639.95
     lat (msec): min=3485, max=10005, avg=5418.02, stdev=1639.98
    clat percentiles (msec):
     |  1.00th=[ 3473],  5.00th=[ 3507], 10.00th=[ 3775], 20.00th=[ 4077],
     | 30.00th=[ 4329], 40.00th=[ 4933], 50.00th=[ 5470], 60.00th=[ 5470],
     | 70.00th=[ 5537], 80.00th=[ 5537], 90.00th=[ 7886], 95.00th=[ 9194],
     | 99.00th=[10000], 99.50th=[10000], 99.90th=[10000], 99.95th=[10000],
     | 99.99th=[10000]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=188708.57, stdev=75166.20, samples=14
   iops        : min=    2, max=  256, avg=184.29, stdev=73.40, samples=14
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.06%, sys=0.06%, ctx=72, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.6%, 16=1.1%, 32=2.3%, >=64=95.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1418,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.6MiB/s (24.8MB/s), 23.6MiB/s-23.6MiB/s (24.8MB/s-24.8MB/s), io=1418MiB (1487MB), run=60026-60026msec

Disk stats (read/write):
  sdb: ios=0/1443, merge=0/14, ticks=0/4311354, in_queue=4310654, util=99.89%
-------------------SIZE:16M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=13.4MiB/s][r=3441 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=106: Thu Jul 21 09:15:22 2022
  read: IOPS=3493, BW=13.6MiB/s (14.3MB/s)(820MiB/60060msec)
    slat (nsec): min=1412, max=315030, avg=5766.39, stdev=3111.68
    clat (usec): min=317, max=393774, avg=36631.56, stdev=24901.84
     lat (usec): min=323, max=393778, avg=36637.50, stdev=24901.90
    clat percentiles (usec):
     |  1.00th=[  1188],  5.00th=[  3064], 10.00th=[  6128], 20.00th=[ 13829],
     | 30.00th=[ 21365], 40.00th=[ 29230], 50.00th=[ 35390], 60.00th=[ 40633],
     | 70.00th=[ 46924], 80.00th=[ 54789], 90.00th=[ 67634], 95.00th=[ 77071],
     | 99.00th=[102237], 99.50th=[133694], 99.90th=[208667], 99.95th=[238027],
     | 99.99th=[287310]
   bw (  KiB/s): min=12024, max=54929, per=99.41%, avg=13890.97, stdev=3867.68, samples=119
   iops        : min= 3006, max=13732, avg=3472.74, stdev=966.90, samples=119
  lat (usec)   : 500=0.03%, 750=0.25%, 1000=0.38%
  lat (msec)   : 2=2.06%, 4=4.03%, 10=8.34%, 20=13.10%, 50=45.91%
  lat (msec)   : 100=24.85%, 250=1.02%, 500=0.04%
  cpu          : usr=1.97%, sys=4.22%, ctx=174755, majf=0, minf=138
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=209819,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=13.6MiB/s (14.3MB/s), 13.6MiB/s-13.6MiB/s (14.3MB/s-14.3MB/s), io=820MiB (859MB), run=60060-60060msec

Disk stats (read/write):
  sdb: ios=185496/3, merge=23809/1, ticks=6914686/79, in_queue=6819621, util=99.97%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=12.0MiB/s][w=3322 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=109: Thu Jul 21 09:16:22 2022
  write: IOPS=3159, BW=12.3MiB/s (12.9MB/s)(741MiB/60044msec); 0 zone resets
    slat (nsec): min=1583, max=63670k, avg=43127.15, stdev=960477.15
    clat (usec): min=854, max=180433, avg=40474.25, stdev=22342.68
     lat (usec): min=865, max=180438, avg=40517.50, stdev=22346.35
    clat percentiles (msec):
     |  1.00th=[    4],  5.00th=[    6], 10.00th=[   12], 20.00th=[   23],
     | 30.00th=[   29], 40.00th=[   34], 50.00th=[   40], 60.00th=[   44],
     | 70.00th=[   49], 80.00th=[   58], 90.00th=[   68], 95.00th=[   85],
     | 99.00th=[  105], 99.50th=[  114], 99.90th=[  131], 99.95th=[  138],
     | 99.99th=[  157]
   bw (  KiB/s): min=10608, max=28104, per=99.87%, avg=12619.23, stdev=1631.24, samples=119
   iops        : min= 2652, max= 7026, avg=3154.81, stdev=407.81, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.10%, 4=2.77%, 10=5.91%, 20=8.67%, 50=54.63%
  lat (msec)   : 100=26.36%, 250=1.56%
  cpu          : usr=0.49%, sys=1.64%, ctx=3322, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,189680,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=12.3MiB/s (12.9MB/s), 12.3MiB/s-12.3MiB/s (12.9MB/s-12.9MB/s), io=741MiB (777MB), run=60044-60044msec

Disk stats (read/write):
  sdb: ios=0/181901, merge=0/14279, ticks=0/2988865, in_queue=2896143, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=112: Thu Jul 21 09:17:29 2022
  read: IOPS=23, BW=23.0MiB/s (25.1MB/s)(1568MiB/65415msec)
    slat (usec): min=12, max=532, avg=47.30, stdev=44.25
    clat (msec): min=15, max=15068, avg=5335.77, stdev=2835.16
     lat (msec): min=15, max=15068, avg=5335.82, stdev=2835.15
    clat percentiles (msec):
     |  1.00th=[   44],  5.00th=[ 1469], 10.00th=[ 1838], 20.00th=[ 2635],
     | 30.00th=[ 3373], 40.00th=[ 4212], 50.00th=[ 5201], 60.00th=[ 6074],
     | 70.00th=[ 7080], 80.00th=[ 8087], 90.00th=[ 9060], 95.00th=[ 9731],
     | 99.00th=[12416], 99.50th=[13624], 99.90th=[14697], 99.95th=[15100],
     | 99.99th=[15100]
   bw (  KiB/s): min=14336, max=81920, per=99.36%, avg=24387.89, stdev=5499.31, samples=120
   iops        : min=   14, max=   80, avg=23.81, stdev= 5.37, samples=120
  lat (msec)   : 20=0.32%, 50=1.15%, 100=1.08%, 250=0.19%, 500=0.38%
  lat (msec)   : 750=0.38%, 1000=0.38%, 2000=8.42%, >=2000=87.69%
  cpu          : usr=0.03%, sys=0.16%, ctx=1569, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.0%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1568,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.0MiB/s (25.1MB/s), 23.0MiB/s-23.0MiB/s (25.1MB/s-25.1MB/s), io=1568MiB (1644MB), run=65415-65415msec

Disk stats (read/write):
  sdb: ios=1563/3, merge=0/1, ticks=7990708/5615, in_queue=7995495, util=99.88%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                       
Fio: (groupid=0, jobs=1): err= 0: pid=115: Thu Jul 21 09:18:33 2022
  write: IOPS=23, BW=23.7MiB/s (24.8MB/s)(1492MiB/62999msec); 0 zone resets
    slat (usec): min=26, max=342, avg=48.22, stdev=21.31
    clat (msec): min=2691, max=11204, avg=5404.34, stdev=1693.52
     lat (msec): min=2691, max=11204, avg=5404.38, stdev=1693.52
    clat percentiles (msec):
     |  1.00th=[ 2702],  5.00th=[ 3272], 10.00th=[ 3675], 20.00th=[ 4077],
     | 30.00th=[ 4530], 40.00th=[ 4665], 50.00th=[ 5067], 60.00th=[ 5470],
     | 70.00th=[ 5470], 80.00th=[ 5470], 90.00th=[ 8658], 95.00th=[ 8792],
     | 99.00th=[ 9329], 99.50th=[11208], 99.90th=[11208], 99.95th=[11208],
     | 99.99th=[11208]
   bw (  KiB/s): min=129024, max=262144, per=100.00%, avg=214882.46, stdev=42249.25, samples=13
   iops        : min=  126, max=  256, avg=209.85, stdev=41.26, samples=13
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.05%, sys=0.07%, ctx=102, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.1%, >=64=95.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1492,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.7MiB/s (24.8MB/s), 23.7MiB/s-23.7MiB/s (24.8MB/s-24.8MB/s), io=1492MiB (1564MB), run=62999-62999msec

Disk stats (read/write):
  sdb: ios=0/1517, merge=0/14, ticks=0/4614218, in_queue=4613468, util=99.86%
-------------------SIZE:32M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=12.3MiB/s][r=3155 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=118: Thu Jul 21 09:19:33 2022
  read: IOPS=3340, BW=13.0MiB/s (13.7MB/s)(784MiB/60064msec)
    slat (nsec): min=1372, max=218100, avg=5992.25, stdev=3251.28
    clat (usec): min=347, max=391799, avg=38307.26, stdev=25908.19
     lat (usec): min=352, max=391806, avg=38313.44, stdev=25908.25
    clat percentiles (usec):
     |  1.00th=[  1254],  5.00th=[  3294], 10.00th=[  6325], 20.00th=[ 14484],
     | 30.00th=[ 22676], 40.00th=[ 31065], 50.00th=[ 36963], 60.00th=[ 42730],
     | 70.00th=[ 49546], 80.00th=[ 57410], 90.00th=[ 70779], 95.00th=[ 80217],
     | 99.00th=[102237], 99.50th=[139461], 99.90th=[221250], 99.95th=[254804],
     | 99.99th=[333448]
   bw (  KiB/s): min=11512, max=52055, per=99.48%, avg=13292.12, stdev=3682.73, samples=119
   iops        : min= 2878, max=13013, avg=3323.02, stdev=920.61, samples=119
  lat (usec)   : 500=0.02%, 750=0.19%, 1000=0.36%
  lat (msec)   : 2=1.93%, 4=3.87%, 10=8.13%, 20=12.25%, 50=44.31%
  lat (msec)   : 100=27.87%, 250=1.01%, 500=0.05%
  cpu          : usr=1.96%, sys=4.11%, ctx=173704, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=200652,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=13.0MiB/s (13.7MB/s), 13.0MiB/s-13.0MiB/s (13.7MB/s-13.7MB/s), io=784MiB (822MB), run=60064-60064msec

Disk stats (read/write):
  sdb: ios=185531/3, merge=14837/1, ticks=7198011/78, in_queue=7100286, util=99.97%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=10.9MiB/s][w=2794 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=121: Thu Jul 21 09:20:34 2022
  write: IOPS=3077, BW=12.0MiB/s (12.6MB/s)(721MiB/60014msec); 0 zone resets
    slat (nsec): min=1583, max=47923k, avg=56811.25, stdev=1018956.88
    clat (usec): min=1087, max=190703, avg=41540.23, stdev=22372.91
     lat (usec): min=1093, max=190706, avg=41597.17, stdev=22363.63
    clat percentiles (msec):
     |  1.00th=[    4],  5.00th=[    8], 10.00th=[   15], 20.00th=[   23],
     | 30.00th=[   29], 40.00th=[   35], 50.00th=[   40], 60.00th=[   45],
     | 70.00th=[   51], 80.00th=[   59], 90.00th=[   70], 95.00th=[   86],
     | 99.00th=[  106], 99.50th=[  113], 99.90th=[  132], 99.95th=[  140],
     | 99.99th=[  161]
   bw (  KiB/s): min=10368, max=26436, per=99.84%, avg=12287.90, stdev=1578.80, samples=119
   iops        : min= 2592, max= 6609, avg=3071.97, stdev=394.70, samples=119
  lat (msec)   : 2=0.15%, 4=1.87%, 10=4.02%, 20=9.74%, 50=54.11%
  lat (msec)   : 100=28.30%, 250=1.82%
  cpu          : usr=0.57%, sys=1.66%, ctx=3559, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,184664,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=12.0MiB/s (12.6MB/s), 12.0MiB/s-12.0MiB/s (12.6MB/s-12.6MB/s), io=721MiB (756MB), run=60014-60014msec

Disk stats (read/write):
  sdb: ios=0/182023, merge=0/9434, ticks=0/2926689, in_queue=2833038, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=124: Thu Jul 21 09:21:41 2022
  read: IOPS=24, BW=24.0MiB/s (25.2MB/s)(1572MiB/65474msec)
    slat (usec): min=12, max=439, avg=43.31, stdev=43.25
    clat (msec): min=15, max=16515, avg=5326.99, stdev=3016.70
     lat (msec): min=15, max=16515, avg=5327.04, stdev=3016.69
    clat percentiles (msec):
     |  1.00th=[   40],  5.00th=[ 1469], 10.00th=[ 1720], 20.00th=[ 2366],
     | 30.00th=[ 3138], 40.00th=[ 4010], 50.00th=[ 5067], 60.00th=[ 6007],
     | 70.00th=[ 7148], 80.00th=[ 8356], 90.00th=[ 9597], 95.00th=[10402],
     | 99.00th=[11745], 99.50th=[12684], 99.90th=[14563], 99.95th=[16576],
     | 99.99th=[16576]
   bw (  KiB/s): min=16384, max=80344, per=99.49%, avg=24460.02, stdev=5300.32, samples=120
   iops        : min=   16, max=   78, avg=23.88, stdev= 5.13, samples=120
  lat (msec)   : 20=0.32%, 50=1.59%, 100=0.51%, 250=0.25%, 500=0.32%
  lat (msec)   : 750=0.38%, 1000=0.38%, 2000=11.07%, >=2000=85.18%
  cpu          : usr=0.03%, sys=0.14%, ctx=1573, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.0%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1572,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=24.0MiB/s (25.2MB/s), 24.0MiB/s-24.0MiB/s (25.2MB/s-25.2MB/s), io=1572MiB (1648MB), run=65474-65474msec

Disk stats (read/write):
  sdb: ios=1566/3, merge=0/1, ticks=7985852/4940, in_queue=7989953, util=99.77%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                       
Fio: (groupid=0, jobs=1): err= 0: pid=127: Thu Jul 21 09:22:44 2022
  write: IOPS=23, BW=23.8MiB/s (24.0MB/s)(1490MiB/62550msec); 0 zone resets
    slat (usec): min=27, max=4493.8k, avg=3411.17, stdev=117174.44
    clat (msec): min=811, max=12726, avg=5368.76, stdev=1584.63
     lat (msec): min=811, max=12726, avg=5372.17, stdev=1579.88
    clat percentiles (msec):
     |  1.00th=[ 3507],  5.00th=[ 3574], 10.00th=[ 3574], 20.00th=[ 4396],
     | 30.00th=[ 5067], 40.00th=[ 5269], 50.00th=[ 5269], 60.00th=[ 5336],
     | 70.00th=[ 5403], 80.00th=[ 5470], 90.00th=[ 8557], 95.00th=[ 8926],
     | 99.00th=[10671], 99.50th=[12684], 99.90th=[12684], 99.95th=[12684],
     | 99.99th=[12684]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=199387.43, stdev=87313.81, samples=14
   iops        : min=    2, max=  256, avg=194.71, stdev=85.27, samples=14
  lat (msec)   : 1000=0.60%, >=2000=99.40%
  cpu          : usr=0.04%, sys=0.08%, ctx=96, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.1%, >=64=95.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1490,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.8MiB/s (24.0MB/s), 23.8MiB/s-23.8MiB/s (24.0MB/s-24.0MB/s), io=1490MiB (1562MB), run=62550-62550msec

Disk stats (read/write):
  sdb: ios=0/1515, merge=0/14, ticks=0/4303218, in_queue=4302465, util=99.88%
-------------------SIZE:64M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=13.5MiB/s][r=3464 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=130: Thu Jul 21 09:23:45 2022
  read: IOPS=3277, BW=12.8MiB/s (13.4MB/s)(769MiB/60059msec)
    slat (nsec): min=1422, max=646633, avg=6139.08, stdev=3882.21
    clat (usec): min=342, max=395773, avg=39046.70, stdev=26683.26
     lat (usec): min=353, max=395776, avg=39053.04, stdev=26683.33
    clat percentiles (usec):
     |  1.00th=[  1188],  5.00th=[  3228], 10.00th=[  6390], 20.00th=[ 14877],
     | 30.00th=[ 23200], 40.00th=[ 31327], 50.00th=[ 37487], 60.00th=[ 43254],
     | 70.00th=[ 50070], 80.00th=[ 57934], 90.00th=[ 71828], 95.00th=[ 82314],
     | 99.00th=[111674], 99.50th=[149947], 99.90th=[231736], 99.95th=[256902],
     | 99.99th=[304088]
   bw (  KiB/s): min=11328, max=55360, per=99.27%, avg=13013.11, stdev=4015.60, samples=119
   iops        : min= 2832, max=13840, avg=3253.28, stdev=1003.90, samples=119
  lat (usec)   : 500=0.01%, 750=0.23%, 1000=0.44%
  lat (msec)   : 2=1.96%, 4=3.85%, 10=7.73%, 20=11.97%, 50=43.78%
  lat (msec)   : 100=28.72%, 250=1.23%, 500=0.06%
  cpu          : usr=2.37%, sys=3.83%, ctx=174926, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=196837,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=12.8MiB/s (13.4MB/s), 12.8MiB/s-12.8MiB/s (13.4MB/s-13.4MB/s), io=769MiB (806MB), run=60059-60059msec

Disk stats (read/write):
  sdb: ios=187162/3, merge=9473/1, ticks=7364249/63, in_queue=7269056, util=99.97%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=12.2MiB/s][w=3127 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=133: Thu Jul 21 09:24:46 2022
  write: IOPS=3051, BW=11.9MiB/s (12.5MB/s)(716MiB/60043msec); 0 zone resets
    slat (nsec): min=1574, max=56477k, avg=47476.38, stdev=1008461.04
    clat (usec): min=1175, max=202622, avg=41894.02, stdev=22519.65
     lat (usec): min=1181, max=202626, avg=41941.62, stdev=22520.74
    clat percentiles (msec):
     |  1.00th=[    3],  5.00th=[    6], 10.00th=[   12], 20.00th=[   24],
     | 30.00th=[   31], 40.00th=[   36], 50.00th=[   41], 60.00th=[   45],
     | 70.00th=[   51], 80.00th=[   60], 90.00th=[   69], 95.00th=[   86],
     | 99.00th=[  105], 99.50th=[  113], 99.90th=[  127], 99.95th=[  136],
     | 99.99th=[  153]
   bw (  KiB/s): min=10160, max=26613, per=99.86%, avg=12188.34, stdev=1575.07, samples=119
   iops        : min= 2540, max= 6653, avg=3047.08, stdev=393.75, samples=119
  lat (msec)   : 2=0.10%, 4=2.76%, 10=5.71%, 20=7.36%, 50=53.82%
  lat (msec)   : 100=28.72%, 250=1.53%
  cpu          : usr=0.50%, sys=1.69%, ctx=3318, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,183236,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=11.9MiB/s (12.5MB/s), 11.9MiB/s-11.9MiB/s (12.5MB/s-12.5MB/s), io=716MiB (751MB), run=60043-60043msec

Disk stats (read/write):
  sdb: ios=0/182638, merge=0/7034, ticks=0/3083994, in_queue=2991060, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=136: Thu Jul 21 09:25:52 2022
  read: IOPS=24, BW=24.1MiB/s (25.2MB/s)(1574MiB/65423msec)
    slat (usec): min=12, max=382, avg=43.89, stdev=35.61
    clat (msec): min=13, max=14791, avg=5316.18, stdev=3213.38
     lat (msec): min=13, max=14791, avg=5316.23, stdev=3213.37
    clat percentiles (msec):
     |  1.00th=[   43],  5.00th=[ 1435], 10.00th=[ 1653], 20.00th=[ 2232],
     | 30.00th=[ 2970], 40.00th=[ 3675], 50.00th=[ 4732], 60.00th=[ 6007],
     | 70.00th=[ 7282], 80.00th=[ 8658], 90.00th=[10000], 95.00th=[10805],
     | 99.00th=[12550], 99.50th=[13624], 99.90th=[14563], 99.95th=[14832],
     | 99.99th=[14832]
   bw (  KiB/s): min=14336, max=88221, per=99.34%, avg=24474.49, stdev=6003.17, samples=120
   iops        : min=   14, max=   86, avg=23.89, stdev= 5.85, samples=120
  lat (msec)   : 20=0.38%, 50=1.21%, 100=1.14%, 250=0.25%, 500=0.38%
  lat (msec)   : 750=0.38%, 1000=0.32%, 2000=11.56%, >=2000=84.37%
  cpu          : usr=0.02%, sys=0.16%, ctx=1573, majf=0, minf=589
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.0%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1574,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=24.1MiB/s (25.2MB/s), 24.1MiB/s-24.1MiB/s (25.2MB/s-25.2MB/s), io=1574MiB (1650MB), run=65423-65423msec

Disk stats (read/write):
  sdb: ios=1569/3, merge=0/1, ticks=7987521/5097, in_queue=7991786, util=99.92%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=139: Thu Jul 21 09:26:58 2022
  write: IOPS=23, BW=23.7MiB/s (24.9MB/s)(1544MiB/65140msec); 0 zone resets
    slat (usec): min=22, max=1002.9k, avg=1113.00, stdev=30221.85
    clat (msec): min=2424, max=11356, avg=5398.78, stdev=1700.71
     lat (msec): min=2424, max=11356, avg=5399.90, stdev=1702.44
    clat percentiles (msec):
     |  1.00th=[ 2433],  5.00th=[ 3708], 10.00th=[ 4044], 20.00th=[ 4329],
     | 30.00th=[ 4530], 40.00th=[ 4732], 50.00th=[ 5067], 60.00th=[ 5134],
     | 70.00th=[ 5470], 80.00th=[ 5470], 90.00th=[ 8926], 95.00th=[ 9463],
     | 99.00th=[10537], 99.50th=[11342], 99.90th=[11342], 99.95th=[11342],
     | 99.99th=[11342]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=193331.20, stdev=72987.98, samples=15
   iops        : min=    2, max=  256, avg=188.80, stdev=71.28, samples=15
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.07%, sys=0.06%, ctx=91, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1544,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.7MiB/s (24.9MB/s), 23.7MiB/s-23.7MiB/s (24.9MB/s-24.9MB/s), io=1544MiB (1619MB), run=65140-65140msec

Disk stats (read/write):
  sdb: ios=0/1567, merge=0/15, ticks=0/4595985, in_queue=4595199, util=99.88%

```
