

### NFS

```
-------------------SIZE:4M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 4MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=20: Thu Jul 21 07:54:16 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1322, max=1122.1k, avg=6479.98, stdev=7716.25
    clat (usec): min=1195, max=28566, avg=5028.70, stdev=838.94
     lat (usec): min=1198, max=28569, avg=5035.37, stdev=839.10
    clat percentiles (usec):
     |  1.00th=[ 3195],  5.00th=[ 3752], 10.00th=[ 4080], 20.00th=[ 4490],
     | 30.00th=[ 4752], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5473], 90.00th=[ 5800], 95.00th=[ 6194],
     | 99.00th=[ 7832], 99.50th=[ 8586], 99.90th=[10683], 99.95th=[11863],
     | 99.99th=[14877]
   bw (  KiB/s): min=85800, max=127240, per=100.00%, avg=101744.65, stdev=6839.09, samples=119
   iops        : min=21450, max=31810, avg=25436.18, stdev=1709.76, samples=119
  lat (msec)   : 2=0.01%, 4=8.72%, 10=91.10%, 20=0.16%, 50=0.01%
  cpu          : usr=5.36%, sys=18.29%, ctx=264943, majf=0, minf=137
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1524939,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=20.1MiB/s][w=5141 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=23: Thu Jul 21 07:55:17 2022
  write: IOPS=5101, BW=19.9MiB/s (20.9MB/s)(1196MiB/60029msec); 0 zone resets
    slat (nsec): min=1533, max=245791, avg=9219.24, stdev=6692.81
    clat (usec): min=4659, max=62352, avg=25080.69, stdev=5958.28
     lat (usec): min=4663, max=62361, avg=25090.13, stdev=5958.27
    clat percentiles (usec):
     |  1.00th=[15008],  5.00th=[16057], 10.00th=[16909], 20.00th=[19006],
     | 30.00th=[20841], 40.00th=[22938], 50.00th=[25035], 60.00th=[27132],
     | 70.00th=[29230], 80.00th=[31065], 90.00th=[32900], 95.00th=[33817],
     | 99.00th=[36439], 99.50th=[38011], 99.90th=[42206], 99.95th=[44827],
     | 99.99th=[53216]
   bw (  KiB/s): min=17432, max=20904, per=100.00%, avg=20432.74, stdev=535.90, samples=119
   iops        : min= 4358, max= 5226, avg=5108.18, stdev=133.97, samples=119
  lat (msec)   : 10=0.01%, 20=25.77%, 50=74.20%, 100=0.02%
  cpu          : usr=1.95%, sys=6.68%, ctx=167168, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,306217,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=19.9MiB/s (20.9MB/s), 19.9MiB/s-19.9MiB/s (20.9MB/s-20.9MB/s), io=1196MiB (1254MB), run=60029-60029msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=253MiB/s][r=252 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=26: Thu Jul 21 07:56:18 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60615msec)
    slat (usec): min=40, max=1360, avg=76.25, stdev=63.15
    clat (msec): min=50, max=1026, avg=537.47, stdev=120.29
     lat (msec): min=51, max=1026, avg=537.55, stdev=120.28
    clat percentiles (msec):
     |  1.00th=[  130],  5.00th=[  355], 10.00th=[  372], 20.00th=[  401],
     | 30.00th=[  439], 40.00th=[  567], 50.00th=[  584], 60.00th=[  600],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  718], 99.50th=[  927], 99.90th=[ 1003], 99.95th=[ 1011],
     | 99.99th=[ 1028]
   bw (  KiB/s): min=120832, max=388740, per=99.74%, avg=243094.43, stdev=57697.80, samples=120
   iops        : min=  118, max=  379, avg=237.39, stdev=56.33, samples=120
  lat (msec)   : 100=0.69%, 250=0.49%, 500=30.79%, 750=67.47%, 1000=0.43%
  lat (msec)   : 2000=0.13%
  cpu          : usr=0.18%, sys=2.13%, ctx=14414, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14427,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60615-60615msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=29: Thu Jul 21 07:57:20 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60538msec); 0 zone resets
    slat (usec): min=58, max=417, avg=104.46, stdev=26.78
    clat (msec): min=16, max=1072, avg=536.43, stdev=42.30
     lat (msec): min=16, max=1072, avg=536.54, stdev=42.30
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  550], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=155648, max=256000, per=99.81%, avg=243779.43, stdev=9363.65, samples=120
   iops        : min=  152, max=  250, avg=238.06, stdev= 9.14, samples=120
  lat (msec)   : 20=0.01%, 50=0.05%, 100=0.09%, 250=0.26%, 500=0.45%
  lat (msec)   : 750=98.61%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.86%, sys=2.20%, ctx=14444, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14439,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60538-60538msec
-------------------SIZE:8M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 8MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=97.8MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=32: Thu Jul 21 07:58:21 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1312, max=1592.2k, avg=6503.78, stdev=7896.29
    clat (usec): min=901, max=30177, avg=5028.51, stdev=1346.42
     lat (usec): min=909, max=30188, avg=5035.24, stdev=1346.50
    clat percentiles (usec):
     |  1.00th=[ 2802],  5.00th=[ 3228], 10.00th=[ 3523], 20.00th=[ 4015],
     | 30.00th=[ 4490], 40.00th=[ 4752], 50.00th=[ 4948], 60.00th=[ 5145],
     | 70.00th=[ 5342], 80.00th=[ 5604], 90.00th=[ 6390], 95.00th=[ 7439],
     | 99.00th=[ 9634], 99.50th=[10814], 99.90th=[15008], 99.95th=[17957],
     | 99.99th=[22676]
   bw (  KiB/s): min=90720, max=126168, per=100.00%, avg=101763.03, stdev=6134.65, samples=119
   iops        : min=22680, max=31542, avg=25440.76, stdev=1533.66, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.03%, 4=19.72%, 10=79.47%, 20=0.75%, 50=0.03%
  cpu          : usr=5.41%, sys=18.47%, ctx=277163, majf=0, minf=138
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1524982,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=17.0MiB/s][w=4354 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=35: Thu Jul 21 07:59:22 2022
  write: IOPS=4240, BW=16.6MiB/s (17.4MB/s)(995MiB/60033msec); 0 zone resets
    slat (nsec): min=1463, max=265037, avg=9317.09, stdev=6544.69
    clat (usec): min=4285, max=72147, avg=30170.21, stdev=8793.57
     lat (usec): min=4315, max=72161, avg=30179.74, stdev=8793.59
    clat percentiles (usec):
     |  1.00th=[15533],  5.00th=[17171], 10.00th=[19006], 20.00th=[22152],
     | 30.00th=[24773], 40.00th=[27132], 50.00th=[29492], 60.00th=[31851],
     | 70.00th=[33817], 80.00th=[37487], 90.00th=[43254], 95.00th=[46400],
     | 99.00th=[51119], 99.50th=[52691], 99.90th=[56886], 99.95th=[58983],
     | 99.99th=[63177]
   bw (  KiB/s): min=15265, max=17784, per=100.00%, avg=16984.88, stdev=442.86, samples=119
   iops        : min= 3816, max= 4446, avg=4246.22, stdev=110.72, samples=119
  lat (msec)   : 10=0.01%, 20=13.23%, 50=85.09%, 100=1.68%
  cpu          : usr=1.65%, sys=5.82%, ctx=147954, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,254593,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=16.6MiB/s (17.4MB/s), 16.6MiB/s-16.6MiB/s (17.4MB/s-17.4MB/s), io=995MiB (1043MB), run=60033-60033msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=238MiB/s][r=237 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=38: Thu Jul 21 08:00:23 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60498msec)
    slat (usec): min=41, max=475, avg=73.00, stdev=27.37
    clat (msec): min=19, max=977, avg=536.65, stdev=120.17
     lat (msec): min=19, max=977, avg=536.72, stdev=120.16
    clat percentiles (msec):
     |  1.00th=[  138],  5.00th=[  355], 10.00th=[  376], 20.00th=[  409],
     | 30.00th=[  439], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  617], 80.00th=[  634], 90.00th=[  659], 95.00th=[  676],
     | 99.00th=[  718], 99.50th=[  751], 99.90th=[  961], 99.95th=[  969],
     | 99.99th=[  978]
   bw (  KiB/s): min=141312, max=370785, per=99.57%, avg=243081.34, stdev=54230.34, samples=120
   iops        : min=  138, max=  362, avg=237.38, stdev=52.96, samples=120
  lat (msec)   : 20=0.01%, 50=0.23%, 100=0.58%, 250=0.35%, 500=32.77%
  lat (msec)   : 750=65.59%, 1000=0.47%
  cpu          : usr=0.17%, sys=2.08%, ctx=14429, majf=0, minf=584
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14424,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60498-60498msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=238MiB/s][w=237 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=41: Thu Jul 21 08:01:24 2022
  write: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60539msec); 0 zone resets
    slat (usec): min=57, max=640, avg=103.30, stdev=26.53
    clat (msec): min=15, max=1071, avg=536.48, stdev=46.78
     lat (msec): min=15, max=1071, avg=536.58, stdev=46.78
    clat percentiles (msec):
     |  1.00th=[  506],  5.00th=[  514], 10.00th=[  514], 20.00th=[  518],
     | 30.00th=[  535], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  550], 95.00th=[  550],
     | 99.00th=[  735], 99.50th=[  768], 99.90th=[ 1020], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=151552, max=258048, per=99.82%, avg=243762.37, stdev=13075.43, samples=120
   iops        : min=  148, max=  252, avg=238.04, stdev=12.77, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.08%, 250=0.27%, 500=0.44%
  lat (msec)   : 750=98.60%, 1000=0.42%, 2000=0.12%
  cpu          : usr=0.91%, sys=2.13%, ctx=14438, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14438,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60539-60539msec
-------------------SIZE:16M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 16MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=44: Thu Jul 21 08:02:25 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1302, max=1471.0k, avg=6429.65, stdev=7794.25
    clat (usec): min=1238, max=22759, avg=5028.86, stdev=705.56
     lat (usec): min=1248, max=22775, avg=5035.49, stdev=705.68
    clat percentiles (usec):
     |  1.00th=[ 3261],  5.00th=[ 3851], 10.00th=[ 4228], 20.00th=[ 4621],
     | 30.00th=[ 4817], 40.00th=[ 4948], 50.00th=[ 5080], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5473], 90.00th=[ 5735], 95.00th=[ 5997],
     | 99.00th=[ 7177], 99.50th=[ 7832], 99.90th=[ 9634], 99.95th=[10421],
     | 99.99th=[13304]
   bw (  KiB/s): min=99320, max=124536, per=100.00%, avg=101766.66, stdev=5287.80, samples=119
   iops        : min=24830, max=31134, avg=25441.66, stdev=1321.95, samples=119
  lat (msec)   : 2=0.01%, 4=6.75%, 10=93.17%, 20=0.07%, 50=0.01%
  cpu          : usr=5.42%, sys=18.38%, ctx=286254, majf=0, minf=137
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1524922,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=14.4MiB/s][w=3679 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=47: Thu Jul 21 08:03:26 2022
  write: IOPS=3708, BW=14.5MiB/s (15.2MB/s)(870MiB/60047msec); 0 zone resets
    slat (nsec): min=1513, max=258134, avg=9393.18, stdev=6416.44
    clat (msec): min=6, max=124, avg=34.51, stdev= 9.85
     lat (msec): min=7, max=124, avg=34.52, stdev= 9.85
    clat percentiles (msec):
     |  1.00th=[   17],  5.00th=[   20], 10.00th=[   23], 20.00th=[   26],
     | 30.00th=[   29], 40.00th=[   32], 50.00th=[   34], 60.00th=[   37],
     | 70.00th=[   40], 80.00th=[   44], 90.00th=[   48], 95.00th=[   52],
     | 99.00th=[   58], 99.50th=[   62], 99.90th=[   73], 99.95th=[   84],
     | 99.99th=[  111]
   bw (  KiB/s): min=12280, max=16680, per=100.00%, avg=14836.98, stdev=1025.60, samples=119
   iops        : min= 3070, max= 4170, avg=3709.24, stdev=256.40, samples=119
  lat (msec)   : 10=0.01%, 20=5.59%, 50=87.85%, 100=6.53%, 250=0.02%
  cpu          : usr=1.50%, sys=5.14%, ctx=131551, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,222664,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=14.5MiB/s (15.2MB/s), 14.5MiB/s-14.5MiB/s (15.2MB/s-15.2MB/s), io=870MiB (912MB), run=60047-60047msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=234MiB/s][r=233 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=50: Thu Jul 21 08:04:28 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60448msec)
    slat (usec): min=41, max=564, avg=73.86, stdev=26.73
    clat (msec): min=16, max=947, avg=536.80, stdev=115.75
     lat (msec): min=16, max=947, avg=536.87, stdev=115.74
    clat percentiles (msec):
     |  1.00th=[  169],  5.00th=[  355], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  493], 40.00th=[  558], 50.00th=[  575], 60.00th=[  592],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  709], 99.50th=[  751], 99.90th=[  936], 99.95th=[  944],
     | 99.99th=[  944]
   bw (  KiB/s): min=135168, max=391901, per=99.46%, avg=242762.38, stdev=58339.65, samples=120
   iops        : min=  132, max=  382, avg=237.07, stdev=56.96, samples=120
  lat (msec)   : 20=0.03%, 50=0.10%, 100=0.50%, 250=0.63%, 500=29.14%
  lat (msec)   : 750=69.18%, 1000=0.42%
  cpu          : usr=0.12%, sys=2.13%, ctx=14419, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14408,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60448-60448msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=53: Thu Jul 21 08:05:29 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60537msec); 0 zone resets
    slat (usec): min=57, max=433, avg=103.80, stdev=25.51
    clat (msec): min=17, max=1072, avg=536.40, stdev=42.36
     lat (msec): min=17, max=1072, avg=536.51, stdev=42.36
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  531],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  550], 95.00th=[  550],
     | 99.00th=[  567], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=157696, max=258048, per=99.81%, avg=243793.12, stdev=9336.90, samples=120
   iops        : min=  154, max=  252, avg=238.08, stdev= 9.12, samples=120
  lat (msec)   : 20=0.01%, 50=0.05%, 100=0.09%, 250=0.27%, 500=0.44%
  lat (msec)   : 750=98.61%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.83%, sys=2.20%, ctx=14447, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14440,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60537-60537msec
-------------------SIZE:32M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 32MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=97.7MiB/s][r=25.0k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=56: Thu Jul 21 08:06:30 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5957MiB/60005msec)
    slat (nsec): min=1323, max=2914.1k, avg=6311.08, stdev=7830.04
    clat (usec): min=1303, max=17975, avg=5028.58, stdev=773.23
     lat (usec): min=1305, max=17988, avg=5035.09, stdev=773.38
    clat percentiles (usec):
     |  1.00th=[ 3261],  5.00th=[ 3818], 10.00th=[ 4146], 20.00th=[ 4490],
     | 30.00th=[ 4752], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5276], 80.00th=[ 5473], 90.00th=[ 5800], 95.00th=[ 6128],
     | 99.00th=[ 7570], 99.50th=[ 8455], 99.90th=[10290], 99.95th=[11207],
     | 99.99th=[13566]
   bw (  KiB/s): min=96192, max=127768, per=100.00%, avg=101729.84, stdev=5907.24, samples=119
   iops        : min=24048, max=31942, avg=25432.45, stdev=1476.80, samples=119
  lat (msec)   : 2=0.01%, 4=7.59%, 10=92.27%, 20=0.13%
  cpu          : usr=5.31%, sys=18.05%, ctx=254878, majf=0, minf=137
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1525031,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5957MiB (6247MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=15.2MiB/s][w=3886 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=59: Thu Jul 21 08:07:31 2022
  write: IOPS=3705, BW=14.5MiB/s (15.2MB/s)(869MiB/60039msec); 0 zone resets
    slat (nsec): min=1532, max=548188, avg=9337.18, stdev=6483.22
    clat (msec): min=4, max=202, avg=34.53, stdev= 9.75
     lat (msec): min=4, max=202, avg=34.54, stdev= 9.75
    clat percentiles (msec):
     |  1.00th=[   18],  5.00th=[   21], 10.00th=[   23], 20.00th=[   26],
     | 30.00th=[   29], 40.00th=[   32], 50.00th=[   34], 60.00th=[   37],
     | 70.00th=[   40], 80.00th=[   44], 90.00th=[   47], 95.00th=[   50],
     | 99.00th=[   54], 99.50th=[   56], 99.90th=[   66], 99.95th=[  171],
     | 99.99th=[  192]
   bw (  KiB/s): min=11176, max=17160, per=100.00%, avg=14820.70, stdev=888.57, samples=119
   iops        : min= 2794, max= 4290, avg=3705.17, stdev=222.14, samples=119
  lat (msec)   : 10=0.01%, 20=4.31%, 50=91.30%, 100=4.33%, 250=0.06%
  cpu          : usr=1.49%, sys=5.14%, ctx=132939, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,222468,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=14.5MiB/s (15.2MB/s), 14.5MiB/s-14.5MiB/s (15.2MB/s-15.2MB/s), io=869MiB (911MB), run=60039-60039msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=255MiB/s][r=254 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=62: Thu Jul 21 08:08:33 2022
  read: IOPS=237, BW=238MiB/s (249MB/s)(14.1GiB/60652msec)
    slat (usec): min=40, max=421, avg=72.69, stdev=25.28
    clat (msec): min=21, max=1059, avg=538.01, stdev=118.17
     lat (msec): min=21, max=1059, avg=538.09, stdev=118.17
    clat percentiles (msec):
     |  1.00th=[  146],  5.00th=[  355], 10.00th=[  368], 20.00th=[  405],
     | 30.00th=[  485], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  726], 99.50th=[  802], 99.90th=[ 1045], 99.95th=[ 1053],
     | 99.99th=[ 1062]
   bw (  KiB/s): min=126976, max=375519, per=99.81%, avg=243069.59, stdev=59744.43, samples=120
   iops        : min=  124, max=  366, avg=237.37, stdev=58.33, samples=120
  lat (msec)   : 50=0.08%, 100=0.39%, 250=0.69%, 500=29.08%, 750=69.22%
  lat (msec)   : 1000=0.21%, 2000=0.34%
  cpu          : usr=0.13%, sys=2.10%, ctx=14437, majf=0, minf=584
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14424,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (249MB/s), 238MiB/s-238MiB/s (249MB/s-249MB/s), io=14.1GiB (15.1GB), run=60652-60652msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=236MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=65: Thu Jul 21 08:09:34 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60537msec); 0 zone resets
    slat (usec): min=57, max=525, avg=103.00, stdev=27.55
    clat (msec): min=17, max=1074, avg=536.44, stdev=42.44
     lat (msec): min=18, max=1074, avg=536.54, stdev=42.44
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  518], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  550], 99.50th=[  768], 99.90th=[ 1020], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=155648, max=258048, per=99.81%, avg=243779.27, stdev=9393.82, samples=120
   iops        : min=  152, max=  252, avg=238.06, stdev= 9.17, samples=120
  lat (msec)   : 20=0.01%, 50=0.05%, 100=0.09%, 250=0.27%, 500=0.44%
  lat (msec)   : 750=98.60%, 1000=0.42%, 2000=0.12%
  cpu          : usr=0.85%, sys=2.18%, ctx=14446, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14439,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60537-60537msec
-------------------SIZE:64M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 64MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=94.8MiB/s][r=24.3k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=68: Thu Jul 21 08:10:35 2022
  read: IOPS=25.4k, BW=99.3MiB/s (104MB/s)(5956MiB/60005msec)
    slat (nsec): min=1332, max=541215, avg=6468.25, stdev=7594.36
    clat (usec): min=1313, max=16916, avg=5028.96, stdev=715.12
     lat (usec): min=1371, max=16922, avg=5035.61, stdev=715.27
    clat percentiles (usec):
     |  1.00th=[ 3458],  5.00th=[ 3916], 10.00th=[ 4178], 20.00th=[ 4490],
     | 30.00th=[ 4686], 40.00th=[ 4883], 50.00th=[ 5014], 60.00th=[ 5145],
     | 70.00th=[ 5342], 80.00th=[ 5538], 90.00th=[ 5866], 95.00th=[ 6194],
     | 99.00th=[ 7046], 99.50th=[ 7504], 99.90th=[ 8848], 99.95th=[ 9896],
     | 99.99th=[13042]
   bw (  KiB/s): min=87448, max=117312, per=100.00%, avg=101721.96, stdev=5058.99, samples=119
   iops        : min=21862, max=29328, avg=25430.49, stdev=1264.75, samples=119
  lat (msec)   : 2=0.01%, 4=6.18%, 10=93.76%, 20=0.05%
  cpu          : usr=5.25%, sys=18.32%, ctx=264370, majf=0, minf=138
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1524851,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=99.3MiB/s (104MB/s), 99.3MiB/s-99.3MiB/s (104MB/s-104MB/s), io=5956MiB (6246MB), run=60005-60005msec
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=13.9MiB/s][w=3557 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=71: Thu Jul 21 08:11:36 2022
  write: IOPS=3638, BW=14.2MiB/s (14.9MB/s)(853MiB/60041msec); 0 zone resets
    slat (nsec): min=1513, max=247325, avg=9733.89, stdev=7008.38
    clat (usec): min=4650, max=89314, avg=35171.16, stdev=8964.59
     lat (usec): min=4678, max=89320, avg=35181.11, stdev=8964.56
    clat percentiles (usec):
     |  1.00th=[17957],  5.00th=[21627], 10.00th=[23725], 20.00th=[26608],
     | 30.00th=[29230], 40.00th=[32113], 50.00th=[34866], 60.00th=[37487],
     | 70.00th=[40633], 80.00th=[43779], 90.00th=[47449], 95.00th=[50070],
     | 99.00th=[53740], 99.50th=[55313], 99.90th=[59507], 99.95th=[62129],
     | 99.99th=[73925]
   bw (  KiB/s): min=13184, max=16392, per=100.00%, avg=14570.90, stdev=613.25, samples=119
   iops        : min= 3296, max= 4098, avg=3642.72, stdev=153.31, samples=119
  lat (msec)   : 10=0.01%, 20=2.89%, 50=92.24%, 100=4.87%
  cpu          : usr=1.73%, sys=4.95%, ctx=133307, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,218433,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=14.2MiB/s (14.9MB/s), 14.2MiB/s-14.2MiB/s (14.9MB/s-14.9MB/s), io=853MiB (895MB), run=60041-60041msec
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=243MiB/s][r=242 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=74: Thu Jul 21 08:12:38 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60449msec)
    slat (usec): min=40, max=1411, avg=75.41, stdev=55.64
    clat (msec): min=49, max=940, avg=536.56, stdev=114.63
     lat (msec): min=49, max=940, avg=536.63, stdev=114.62
    clat percentiles (msec):
     |  1.00th=[  144],  5.00th=[  355], 10.00th=[  372], 20.00th=[  405],
     | 30.00th=[  472], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  651], 95.00th=[  667],
     | 99.00th=[  701], 99.50th=[  709], 99.90th=[  927], 99.95th=[  936],
     | 99.99th=[  936]
   bw (  KiB/s): min=143360, max=377097, per=99.48%, avg=242877.94, stdev=54895.19, samples=120
   iops        : min=  140, max=  368, avg=237.18, stdev=53.60, samples=120
  lat (msec)   : 50=0.01%, 100=0.41%, 250=0.76%, 500=29.27%, 750=69.20%
  lat (msec)   : 1000=0.35%
  cpu          : usr=0.12%, sys=2.17%, ctx=14424, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14413,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60449-60449msec
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=237 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=77: Thu Jul 21 08:13:39 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60538msec); 0 zone resets
    slat (usec): min=57, max=497, avg=101.78, stdev=26.11
    clat (msec): min=16, max=1069, avg=536.41, stdev=42.40
     lat (msec): min=16, max=1069, avg=536.51, stdev=42.40
    clat percentiles (msec):
     |  1.00th=[  510],  5.00th=[  514], 10.00th=[  514], 20.00th=[  531],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  550],
     | 99.00th=[  567], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=155648, max=258048, per=99.81%, avg=243793.12, stdev=9471.83, samples=120
   iops        : min=  152, max=  252, avg=238.07, stdev= 9.25, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.08%, 250=0.27%, 500=0.44%
  lat (msec)   : 750=98.60%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.88%, sys=2.09%, ctx=14449, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14440,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60538-60538msec

```


### 块设备


```
-------------------SIZE:4M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 4MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=15.6MiB/s][r=3996 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=20: Thu Jul 21 08:30:22 2022
  read: IOPS=4191, BW=16.4MiB/s (17.2MB/s)(983MiB/60056msec)
    slat (nsec): min=1342, max=353211, avg=5478.66, stdev=3615.21
    clat (usec): min=281, max=250072, avg=30529.90, stdev=21049.77
     lat (usec): min=288, max=250076, avg=30535.56, stdev=21049.86
    clat percentiles (usec):
     |  1.00th=[   996],  5.00th=[  2376], 10.00th=[  4883], 20.00th=[ 10814],
     | 30.00th=[ 16712], 40.00th=[ 22676], 50.00th=[ 29230], 60.00th=[ 34341],
     | 70.00th=[ 39584], 80.00th=[ 47449], 90.00th=[ 57934], 95.00th=[ 64750],
     | 99.00th=[ 87557], 99.50th=[111674], 99.90th=[156238], 99.95th=[173016],
     | 99.99th=[206570]
   bw (  KiB/s): min=15088, max=59169, per=99.67%, avg=16710.39, stdev=3947.20, samples=119
   iops        : min= 3772, max=14792, avg=4177.60, stdev=986.78, samples=119
  lat (usec)   : 500=0.06%, 750=0.35%, 1000=0.60%
  lat (msec)   : 2=2.86%, 4=4.64%, 10=10.11%, 20=16.81%, 50=47.31%
  lat (msec)   : 100=16.56%, 250=0.71%, 500=0.01%
  cpu          : usr=2.23%, sys=4.44%, ctx=171792, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=251725,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=16.4MiB/s (17.2MB/s), 16.4MiB/s-16.4MiB/s (17.2MB/s-17.2MB/s), io=983MiB (1031MB), run=60056-60056msec

Disk stats (read/write):
  sdb: ios=184605/7, merge=63479/2, ticks=5777771/163, in_queue=5681319, util=99.97%
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=21.8MiB/s][w=5591 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=23: Thu Jul 21 08:31:23 2022
  write: IOPS=5865, BW=22.9MiB/s (24.0MB/s)(1375MiB/60008msec); 0 zone resets
    slat (nsec): min=1532, max=28227k, avg=24673.37, stdev=404515.66
    clat (usec): min=331, max=61915, avg=21795.98, stdev=11793.61
     lat (usec): min=338, max=61919, avg=21820.81, stdev=11784.19
    clat percentiles (usec):
     |  1.00th=[ 1221],  5.00th=[ 1549], 10.00th=[ 2180], 20.00th=[ 8979],
     | 30.00th=[18220], 40.00th=[21627], 50.00th=[22676], 60.00th=[24511],
     | 70.00th=[27395], 80.00th=[32637], 90.00th=[36963], 95.00th=[39584],
     | 99.00th=[44827], 99.50th=[46400], 99.90th=[52691], 99.95th=[53740],
     | 99.99th=[56886]
   bw (  KiB/s): min=21656, max=61473, per=99.75%, avg=23402.50, stdev=3807.35, samples=119
   iops        : min= 5414, max=15368, avg=5850.62, stdev=951.82, samples=119
  lat (usec)   : 500=0.01%, 750=0.02%, 1000=0.15%
  lat (msec)   : 2=8.79%, 4=4.98%, 10=7.20%, 20=10.73%, 50=67.96%
  lat (msec)   : 100=0.16%
  cpu          : usr=1.06%, sys=4.03%, ctx=8752, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,351984,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=22.9MiB/s (24.0MB/s), 22.9MiB/s-22.9MiB/s (24.0MB/s-24.0MB/s), io=1375MiB (1442MB), run=60008-60008msec

Disk stats (read/write):
  sdb: ios=0/162967, merge=0/208251, ticks=0/738314, in_queue=644270, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=26: Thu Jul 21 08:32:30 2022
  read: IOPS=23, BW=23.6MiB/s (24.7MB/s)(1544MiB/65495msec)
    slat (usec): min=12, max=396, avg=47.73, stdev=45.90
    clat (msec): min=16, max=12551, avg=5425.28, stdev=1707.42
     lat (msec): min=16, max=12551, avg=5425.33, stdev=1707.41
    clat percentiles (msec):
     |  1.00th=[   39],  5.00th=[ 2433], 10.00th=[ 3742], 20.00th=[ 4396],
     | 30.00th=[ 4866], 40.00th=[ 5134], 50.00th=[ 5537], 60.00th=[ 5738],
     | 70.00th=[ 6141], 80.00th=[ 6544], 90.00th=[ 7148], 95.00th=[ 7617],
     | 99.00th=[10537], 99.50th=[11342], 99.90th=[12550], 99.95th=[12550],
     | 99.99th=[12550]
   bw (  KiB/s): min=14336, max=55138, per=99.61%, avg=24045.20, stdev=3233.44, samples=120
   iops        : min=   14, max=   53, avg=23.47, stdev= 3.09, samples=120
  lat (msec)   : 20=0.19%, 50=1.23%, 100=0.06%, 250=0.19%, 500=0.39%
  lat (msec)   : 750=0.39%, 1000=0.39%, 2000=1.42%, >=2000=95.73%
  cpu          : usr=0.02%, sys=0.17%, ctx=1542, majf=0, minf=585
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1544,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.6MiB/s (24.7MB/s), 23.6MiB/s-23.6MiB/s (24.7MB/s-24.7MB/s), io=1544MiB (1619MB), run=65495-65495msec

Disk stats (read/write):
  sdb: ios=1543/3, merge=0/1, ticks=8025391/5841, in_queue=8030438, util=99.85%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                       
Fio: (groupid=0, jobs=1): err= 0: pid=29: Thu Jul 21 08:33:33 2022
  write: IOPS=23, BW=23.6MiB/s (24.8MB/s)(1482MiB/62780msec); 0 zone resets
    slat (usec): min=26, max=991272, avg=1319.13, stdev=34559.33
    clat (msec): min=2404, max=10756, avg=5420.67, stdev=1499.46
     lat (msec): min=2404, max=10756, avg=5421.99, stdev=1499.03
    clat percentiles (msec):
     |  1.00th=[ 2400],  5.00th=[ 2400], 10.00th=[ 4144], 20.00th=[ 4178],
     | 30.00th=[ 5403], 40.00th=[ 5403], 50.00th=[ 5403], 60.00th=[ 5537],
     | 70.00th=[ 5537], 80.00th=[ 5537], 90.00th=[ 7819], 95.00th=[ 8423],
     | 99.00th=[ 9731], 99.50th=[10671], 99.90th=[10805], 99.95th=[10805],
     | 99.99th=[10805]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=198070.86, stdev=80383.09, samples=14
   iops        : min=    2, max=  256, avg=193.43, stdev=78.50, samples=14
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.07%, sys=0.06%, ctx=120, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.2%, >=64=95.7%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1482,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.6MiB/s (24.8MB/s), 23.6MiB/s-23.6MiB/s (24.8MB/s-24.8MB/s), io=1482MiB (1554MB), run=62780-62780msec

Disk stats (read/write):
  sdb: ios=0/1507, merge=0/14, ticks=0/4361091, in_queue=4360339, util=99.91%
-------------------SIZE:8M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 8MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=14.0MiB/s][r=3593 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=32: Thu Jul 21 08:34:34 2022
  read: IOPS=3735, BW=14.6MiB/s (15.3MB/s)(876MiB/60059msec)
    slat (nsec): min=1392, max=290325, avg=5652.03, stdev=3724.13
    clat (usec): min=290, max=344773, avg=34254.47, stdev=23238.23
     lat (usec): min=298, max=344775, avg=34260.30, stdev=23238.27
    clat percentiles (usec):
     |  1.00th=[  1090],  5.00th=[  3032], 10.00th=[  6390], 20.00th=[ 13173],
     | 30.00th=[ 19792], 40.00th=[ 26608], 50.00th=[ 32900], 60.00th=[ 38011],
     | 70.00th=[ 43779], 80.00th=[ 51119], 90.00th=[ 63701], 95.00th=[ 72877],
     | 99.00th=[ 96994], 99.50th=[126354], 99.90th=[193987], 99.95th=[219153],
     | 99.99th=[270533]
   bw (  KiB/s): min=13632, max=45957, per=99.83%, avg=14918.05, stdev=3108.57, samples=119
   iops        : min= 3408, max=11489, avg=3729.50, stdev=777.12, samples=119
  lat (usec)   : 500=0.03%, 750=0.29%, 1000=0.49%
  lat (msec)   : 2=2.09%, 4=3.66%, 10=8.64%, 20=14.95%, 50=48.41%
  lat (msec)   : 100=20.52%, 250=0.90%, 500=0.02%
  cpu          : usr=2.03%, sys=4.16%, ctx=174615, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=224368,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=14.6MiB/s (15.3MB/s), 14.6MiB/s-14.6MiB/s (15.3MB/s-15.3MB/s), io=876MiB (919MB), run=60059-60059msec

Disk stats (read/write):
  sdb: ios=184485/7, merge=38544/2, ticks=6473553/164, in_queue=6379214, util=99.96%
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=21.7MiB/s][w=5562 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=35: Thu Jul 21 08:35:35 2022
  write: IOPS=5785, BW=22.6MiB/s (23.7MB/s)(1357MiB/60020msec); 0 zone resets
    slat (nsec): min=1522, max=30824k, avg=22785.91, stdev=437453.52
    clat (usec): min=315, max=66208, avg=22098.61, stdev=12598.54
     lat (usec): min=338, max=66212, avg=22121.55, stdev=12591.55
    clat percentiles (usec):
     |  1.00th=[ 1188],  5.00th=[ 1483], 10.00th=[ 1975], 20.00th=[ 7308],
     | 30.00th=[18220], 40.00th=[21627], 50.00th=[22414], 60.00th=[24511],
     | 70.00th=[28967], 80.00th=[33817], 90.00th=[38011], 95.00th=[41681],
     | 99.00th=[46924], 99.50th=[49546], 99.90th=[53216], 99.95th=[54789],
     | 99.99th=[59507]
   bw (  KiB/s): min=21528, max=60449, per=99.75%, avg=23084.58, stdev=3655.03, samples=119
   iops        : min= 5382, max=15112, avg=5771.14, stdev=913.73, samples=119
  lat (usec)   : 500=0.02%, 750=0.04%, 1000=0.18%
  lat (msec)   : 2=9.97%, 4=4.92%, 10=7.94%, 20=8.30%, 50=68.29%
  lat (msec)   : 100=0.35%
  cpu          : usr=1.10%, sys=3.83%, ctx=8944, majf=0, minf=14
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,347272,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=22.6MiB/s (23.7MB/s), 22.6MiB/s-22.6MiB/s (23.7MB/s-23.7MB/s), io=1357MiB (1422MB), run=60020-60020msec

Disk stats (read/write):
  sdb: ios=0/161809, merge=0/206246, ticks=0/784836, in_queue=692347, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=38: Thu Jul 21 08:36:42 2022
  read: IOPS=23, BW=23.6MiB/s (24.7MB/s)(1544MiB/65506msec)
    slat (usec): min=12, max=515, avg=50.70, stdev=42.38
    clat (msec): min=15, max=14747, avg=5426.23, stdev=2260.32
     lat (msec): min=15, max=14747, avg=5426.28, stdev=2260.31
    clat percentiles (msec):
     |  1.00th=[   32],  5.00th=[ 1787], 10.00th=[ 2500], 20.00th=[ 3540],
     | 30.00th=[ 4279], 40.00th=[ 4866], 50.00th=[ 5470], 60.00th=[ 6007],
     | 70.00th=[ 6544], 80.00th=[ 7349], 90.00th=[ 8288], 95.00th=[ 9060],
     | 99.00th=[10805], 99.50th=[12013], 99.90th=[14160], 99.95th=[14697],
     | 99.99th=[14697]
   bw (  KiB/s): min=14336, max=55138, per=99.63%, avg=24045.62, stdev=3244.39, samples=120
   iops        : min=   14, max=   53, avg=23.47, stdev= 3.10, samples=120
  lat (msec)   : 20=0.39%, 50=0.97%, 100=0.13%, 250=0.19%, 500=0.39%
  lat (msec)   : 750=0.39%, 1000=0.45%, 2000=3.30%, >=2000=93.78%
  cpu          : usr=0.03%, sys=0.17%, ctx=1541, majf=0, minf=586
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1544,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.6MiB/s (24.7MB/s), 23.6MiB/s-23.6MiB/s (24.7MB/s-24.7MB/s), io=1544MiB (1619MB), run=65506-65506msec

Disk stats (read/write):
  sdb: ios=1543/3, merge=0/1, ticks=8027121/5819, in_queue=8032139, util=99.92%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=1022KiB/s][w=0 IOPS][eta 00m:00s] 
Fio: (groupid=0, jobs=1): err= 0: pid=41: Thu Jul 21 08:37:47 2022
  write: IOPS=23, BW=23.6MiB/s (24.7MB/s)(1522MiB/64514msec); 0 zone resets
    slat (usec): min=27, max=409, avg=50.04, stdev=22.15
    clat (msec): min=2400, max=10892, avg=5424.51, stdev=1549.20
     lat (msec): min=2400, max=10892, avg=5424.56, stdev=1549.20
    clat percentiles (msec):
     |  1.00th=[ 2400],  5.00th=[ 2802], 10.00th=[ 3842], 20.00th=[ 4396],
     | 30.00th=[ 4463], 40.00th=[ 5403], 50.00th=[ 5537], 60.00th=[ 5537],
     | 70.00th=[ 5537], 80.00th=[ 6879], 90.00th=[ 7819], 95.00th=[ 8020],
     | 99.00th=[10268], 99.50th=[10268], 99.90th=[10939], 99.95th=[10939],
     | 99.99th=[10939]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=190464.00, stdev=72877.89, samples=15
   iops        : min=    2, max=  256, avg=186.00, stdev=71.17, samples=15
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.07%, sys=0.05%, ctx=88, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1522,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.6MiB/s (24.7MB/s), 23.6MiB/s-23.6MiB/s (24.7MB/s-24.7MB/s), io=1522MiB (1596MB), run=64514-64514msec

Disk stats (read/write):
  sdb: ios=0/1550, merge=0/15, ticks=0/4808305, in_queue=4807535, util=99.89%
-------------------SIZE:16M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 16MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=13.2MiB/s][r=3380 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=44: Thu Jul 21 08:38:48 2022
  read: IOPS=3492, BW=13.6MiB/s (14.3MB/s)(819MiB/60055msec)
    slat (nsec): min=1393, max=249548, avg=5827.94, stdev=3222.92
    clat (usec): min=296, max=418220, avg=36640.50, stdev=24511.49
     lat (usec): min=300, max=418227, avg=36646.53, stdev=24511.55
    clat percentiles (usec):
     |  1.00th=[  1221],  5.00th=[  3687], 10.00th=[  7308], 20.00th=[ 14484],
     | 30.00th=[ 21890], 40.00th=[ 28967], 50.00th=[ 34866], 60.00th=[ 40633],
     | 70.00th=[ 46400], 80.00th=[ 54789], 90.00th=[ 67634], 95.00th=[ 77071],
     | 99.00th=[101188], 99.50th=[133694], 99.90th=[206570], 99.95th=[235930],
     | 99.99th=[304088]
   bw (  KiB/s): min=11960, max=35449, per=99.95%, avg=13963.64, stdev=2500.87, samples=119
   iops        : min= 2990, max= 8862, avg=3490.91, stdev=625.20, samples=119
  lat (usec)   : 500=0.03%, 750=0.27%, 1000=0.36%
  lat (msec)   : 2=1.66%, 4=3.14%, 10=8.28%, 20=13.76%, 50=47.22%
  lat (msec)   : 100=24.26%, 250=0.99%, 500=0.03%
  cpu          : usr=2.20%, sys=4.15%, ctx=176755, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=209743,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=13.6MiB/s (14.3MB/s), 13.6MiB/s-13.6MiB/s (14.3MB/s-14.3MB/s), io=819MiB (859MB), run=60055-60055msec

Disk stats (read/write):
  sdb: ios=185117/7, merge=23841/2, ticks=6913176/95, in_queue=6819272, util=99.97%
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=21.0MiB/s][w=5629 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=47: Thu Jul 21 08:39:49 2022
  write: IOPS=5818, BW=22.7MiB/s (23.8MB/s)(1364MiB/60009msec); 0 zone resets
    slat (nsec): min=1522, max=30309k, avg=20614.68, stdev=400831.23
    clat (usec): min=319, max=62263, avg=21976.22, stdev=12821.93
     lat (usec): min=334, max=62294, avg=21996.99, stdev=12815.66
    clat percentiles (usec):
     |  1.00th=[ 1156],  5.00th=[ 1418], 10.00th=[ 1827], 20.00th=[ 6783],
     | 30.00th=[17695], 40.00th=[21627], 50.00th=[22414], 60.00th=[24249],
     | 70.00th=[29230], 80.00th=[33817], 90.00th=[38536], 95.00th=[41681],
     | 99.00th=[46924], 99.50th=[49021], 99.90th=[54264], 99.95th=[55837],
     | 99.99th=[61604]
   bw (  KiB/s): min=21392, max=59587, per=99.76%, avg=23217.13, stdev=3584.34, samples=119
   iops        : min= 5348, max=14896, avg=5804.27, stdev=896.02, samples=119
  lat (usec)   : 500=0.02%, 750=0.03%, 1000=0.23%
  lat (msec)   : 2=10.89%, 4=4.69%, 10=8.02%, 20=8.77%, 50=67.03%
  lat (msec)   : 100=0.32%
  cpu          : usr=1.08%, sys=3.82%, ctx=9081, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,349173,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=22.7MiB/s (23.8MB/s), 22.7MiB/s-22.7MiB/s (23.8MB/s-23.8MB/s), io=1364MiB (1430MB), run=60009-60009msec

Disk stats (read/write):
  sdb: ios=0/164682, merge=0/205940, ticks=0/807885, in_queue=713636, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=50: Thu Jul 21 08:40:55 2022
  read: IOPS=23, BW=23.7MiB/s (24.9MB/s)(1552MiB/65451msec)
    slat (usec): min=12, max=422, avg=47.47, stdev=41.37
    clat (msec): min=15, max=14175, avg=5393.73, stdev=2698.38
     lat (msec): min=15, max=14175, avg=5393.78, stdev=2698.38
    clat percentiles (msec):
     |  1.00th=[   28],  5.00th=[ 1536], 10.00th=[ 1955], 20.00th=[ 2735],
     | 30.00th=[ 3608], 40.00th=[ 4396], 50.00th=[ 5269], 60.00th=[ 6141],
     | 70.00th=[ 7080], 80.00th=[ 8020], 90.00th=[ 9060], 95.00th=[ 9597],
     | 99.00th=[11745], 99.50th=[12684], 99.90th=[14026], 99.95th=[14160],
     | 99.99th=[14160]
   bw (  KiB/s): min=16384, max=56713, per=99.58%, avg=24178.21, stdev=3330.51, samples=120
   iops        : min=   16, max=   55, avg=23.61, stdev= 3.22, samples=120
  lat (msec)   : 20=0.39%, 50=1.03%, 100=0.06%, 250=0.19%, 500=0.39%
  lat (msec)   : 750=0.45%, 1000=0.32%, 2000=8.18%, >=2000=88.98%
  cpu          : usr=0.03%, sys=0.16%, ctx=1552, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1552,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.7MiB/s (24.9MB/s), 23.7MiB/s-23.7MiB/s (24.9MB/s-24.9MB/s), io=1552MiB (1627MB), run=65451-65451msec

Disk stats (read/write):
  sdb: ios=1546/3, merge=0/1, ticks=7991702/5453, in_queue=7996336, util=99.80%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=1022KiB/s][w=0 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=53: Thu Jul 21 08:41:59 2022
  write: IOPS=23, BW=23.7MiB/s (24.8MB/s)(1503MiB/63507msec); 0 zone resets
    slat (usec): min=26, max=4255.2k, avg=3223.66, stdev=110555.05
    clat (msec): min=722, max=10687, avg=5404.71, stdev=1468.66
     lat (msec): min=3710, max=10687, avg=5407.94, stdev=1463.38
    clat percentiles (msec):
     |  1.00th=[ 3708],  5.00th=[ 3708], 10.00th=[ 4279], 20.00th=[ 4665],
     | 30.00th=[ 4799], 40.00th=[ 4933], 50.00th=[ 5000], 60.00th=[ 5201],
     | 70.00th=[ 5470], 80.00th=[ 5470], 90.00th=[ 8557], 95.00th=[ 9597],
     | 99.00th=[10402], 99.50th=[10402], 99.90th=[10671], 99.95th=[10671],
     | 99.99th=[10671]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=201142.86, stdev=82856.64, samples=14
   iops        : min=    2, max=  256, avg=196.43, stdev=80.91, samples=14
  lat (msec)   : 750=0.07%, >=2000=99.93%
  cpu          : usr=0.06%, sys=0.06%, ctx=81, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.1%, >=64=95.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1503,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.7MiB/s (24.8MB/s), 23.7MiB/s-23.7MiB/s (24.8MB/s-24.8MB/s), io=1503MiB (1576MB), run=63507-63507msec

Disk stats (read/write):
  sdb: ios=0/1529, merge=0/14, ticks=0/4405978, in_queue=4405191, util=99.87%
-------------------SIZE:32M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 32MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=13.3MiB/s][r=3417 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=56: Thu Jul 21 08:43:01 2022
  read: IOPS=3345, BW=13.1MiB/s (13.7MB/s)(785MiB/60066msec)
    slat (nsec): min=1393, max=318297, avg=6037.99, stdev=3725.85
    clat (usec): min=305, max=423017, avg=38255.40, stdev=25062.85
     lat (usec): min=315, max=423024, avg=38261.63, stdev=25062.88
    clat percentiles (usec):
     |  1.00th=[  1270],  5.00th=[  4080], 10.00th=[  7963], 20.00th=[ 15664],
     | 30.00th=[ 22938], 40.00th=[ 30540], 50.00th=[ 36439], 60.00th=[ 42206],
     | 70.00th=[ 48497], 80.00th=[ 56886], 90.00th=[ 69731], 95.00th=[ 80217],
     | 99.00th=[102237], 99.50th=[133694], 99.90th=[206570], 99.95th=[233833],
     | 99.99th=[295699]
   bw (  KiB/s): min=11440, max=27992, per=100.00%, avg=13402.96, stdev=2307.49, samples=119
   iops        : min= 2860, max= 6998, avg=3350.74, stdev=576.87, samples=119
  lat (usec)   : 500=0.03%, 750=0.22%, 1000=0.36%
  lat (msec)   : 2=1.50%, 4=2.80%, 10=7.76%, 20=13.29%, 50=45.88%
  lat (msec)   : 100=27.07%, 250=1.05%, 500=0.04%
  cpu          : usr=2.13%, sys=4.09%, ctx=177876, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=200924,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=13.1MiB/s (13.7MB/s), 13.1MiB/s-13.1MiB/s (13.7MB/s-13.7MB/s), io=785MiB (823MB), run=60066-60066msec

Disk stats (read/write):
  sdb: ios=185570/7, merge=14762/2, ticks=7190771/190, in_queue=7096450, util=99.97%
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=21.7MiB/s][w=5546 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=59: Thu Jul 21 08:44:02 2022
  write: IOPS=5810, BW=22.7MiB/s (23.8MB/s)(1362MiB/60023msec); 0 zone resets
    slat (nsec): min=1532, max=29967k, avg=19360.38, stdev=388205.94
    clat (usec): min=324, max=61868, avg=22008.05, stdev=12364.22
     lat (usec): min=329, max=61874, avg=22027.56, stdev=12358.02
    clat percentiles (usec):
     |  1.00th=[ 1188],  5.00th=[ 1500], 10.00th=[ 2073], 20.00th=[ 8160],
     | 30.00th=[17957], 40.00th=[21627], 50.00th=[22152], 60.00th=[24249],
     | 70.00th=[28705], 80.00th=[32900], 90.00th=[38536], 95.00th=[41157],
     | 99.00th=[46924], 99.50th=[49546], 99.90th=[52167], 99.95th=[54264],
     | 99.99th=[56886]
   bw (  KiB/s): min=21304, max=55007, per=99.80%, avg=23194.96, stdev=3187.00, samples=119
   iops        : min= 5326, max=13751, avg=5798.73, stdev=796.69, samples=119
  lat (usec)   : 500=0.02%, 750=0.02%, 1000=0.15%
  lat (msec)   : 2=9.35%, 4=4.41%, 10=8.27%, 20=9.81%, 50=67.64%
  lat (msec)   : 100=0.31%
  cpu          : usr=1.04%, sys=3.88%, ctx=8701, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,348768,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=22.7MiB/s (23.8MB/s), 22.7MiB/s-22.7MiB/s (23.8MB/s-23.8MB/s), io=1362MiB (1429MB), run=60023-60023msec

Disk stats (read/write):
  sdb: ios=0/160077, merge=0/209462, ticks=0/793341, in_queue=702904, util=99.95%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=62: Thu Jul 21 08:45:08 2022
  read: IOPS=23, BW=23.7MiB/s (24.9MB/s)(1552MiB/65466msec)
    slat (usec): min=13, max=374, avg=48.00, stdev=31.55
    clat (msec): min=12, max=16747, avg=5395.13, stdev=2989.76
     lat (msec): min=12, max=16747, avg=5395.18, stdev=2989.75
    clat percentiles (msec):
     |  1.00th=[   31],  5.00th=[ 1519], 10.00th=[ 1804], 20.00th=[ 2467],
     | 30.00th=[ 3205], 40.00th=[ 4144], 50.00th=[ 5000], 60.00th=[ 6007],
     | 70.00th=[ 7215], 80.00th=[ 8221], 90.00th=[ 9597], 95.00th=[10402],
     | 99.00th=[12818], 99.50th=[14026], 99.90th=[15637], 99.95th=[16711],
     | 99.99th=[16711]
   bw (  KiB/s): min=14336, max=55138, per=99.62%, avg=24182.15, stdev=3165.26, samples=120
   iops        : min=   14, max=   53, avg=23.61, stdev= 3.02, samples=120
  lat (msec)   : 20=0.32%, 50=1.03%, 100=0.13%, 250=0.19%, 500=0.39%
  lat (msec)   : 750=0.39%, 1000=0.39%, 2000=10.24%, >=2000=86.92%
  cpu          : usr=0.03%, sys=0.17%, ctx=1550, majf=0, minf=587
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1552,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.7MiB/s (24.9MB/s), 23.7MiB/s-23.7MiB/s (24.9MB/s-24.9MB/s), io=1552MiB (1627MB), run=65466-65466msec

Disk stats (read/write):
  sdb: ios=1546/3, merge=0/1, ticks=7989051/5658, in_queue=7993893, util=99.87%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=65: Thu Jul 21 08:46:14 2022
  write: IOPS=23, BW=23.7MiB/s (24.9MB/s)(1545MiB/65070msec); 0 zone resets
    slat (usec): min=23, max=3623.1k, avg=16246.54, stdev=205491.06
    clat (msec): min=1448, max=11248, avg=5372.38, stdev=1393.92
     lat (msec): min=1449, max=11248, avg=5388.62, stdev=1398.38
    clat percentiles (msec):
     |  1.00th=[ 3004],  5.00th=[ 4279], 10.00th=[ 4396], 20.00th=[ 4463],
     | 30.00th=[ 4866], 40.00th=[ 4866], 50.00th=[ 5000], 60.00th=[ 5201],
     | 70.00th=[ 5470], 80.00th=[ 5470], 90.00th=[ 7550], 95.00th=[ 9194],
     | 99.00th=[10268], 99.50th=[10402], 99.90th=[10402], 99.95th=[11208],
     | 99.99th=[11208]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=120986.79, stdev=105170.29, samples=24
   iops        : min=    2, max=  256, avg=118.12, stdev=102.69, samples=24
  lat (msec)   : 2000=0.19%, >=2000=99.81%
  cpu          : usr=0.07%, sys=0.06%, ctx=139, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1545,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.7MiB/s (24.9MB/s), 23.7MiB/s-23.7MiB/s (24.9MB/s-24.9MB/s), io=1545MiB (1620MB), run=65070-65070msec

Disk stats (read/write):
  sdb: ios=0/1583, merge=0/20, ticks=0/4036205, in_queue=4035400, util=99.82%
-------------------SIZE:64M-------------------------
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 64MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=12.2MiB/s][r=3117 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=68: Thu Jul 21 08:47:17 2022
  read: IOPS=3233, BW=12.6MiB/s (13.2MB/s)(759MiB/60066msec)
    slat (nsec): min=1403, max=362048, avg=6323.13, stdev=3829.97
    clat (usec): min=322, max=390979, avg=39572.54, stdev=25884.69
     lat (usec): min=326, max=390988, avg=39579.06, stdev=25884.71
    clat percentiles (usec):
     |  1.00th=[  1336],  5.00th=[  4359], 10.00th=[  8291], 20.00th=[ 16319],
     | 30.00th=[ 23987], 40.00th=[ 31851], 50.00th=[ 38011], 60.00th=[ 43779],
     | 70.00th=[ 50070], 80.00th=[ 58459], 90.00th=[ 71828], 95.00th=[ 82314],
     | 99.00th=[106431], 99.50th=[143655], 99.90th=[217056], 99.95th=[248513],
     | 99.99th=[295699]
   bw (  KiB/s): min=11424, max=27544, per=99.94%, avg=12926.52, stdev=2094.11, samples=119
   iops        : min= 2856, max= 6886, avg=3231.63, stdev=523.53, samples=119
  lat (usec)   : 500=0.02%, 750=0.18%, 1000=0.31%
  lat (msec)   : 2=1.42%, 4=2.63%, 10=7.53%, 20=12.64%, 50=44.79%
  lat (msec)   : 100=29.26%, 250=1.15%, 500=0.05%
  cpu          : usr=2.44%, sys=4.00%, ctx=177452, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=194231,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=12.6MiB/s (13.2MB/s), 12.6MiB/s-12.6MiB/s (13.2MB/s-13.2MB/s), io=759MiB (796MB), run=60066-60066msec

Disk stats (read/write):
  sdb: ios=184857/7, merge=9112/3, ticks=7370976/157, in_queue=7276312, util=99.96%
----------------------
Fio: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [W(1)][100.0%][w=22.5MiB/s][w=5759 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=71: Thu Jul 21 08:48:18 2022
  write: IOPS=5867, BW=22.9MiB/s (24.0MB/s)(1376MiB/60017msec); 0 zone resets
    slat (nsec): min=1513, max=28886k, avg=17346.87, stdev=357635.79
    clat (usec): min=317, max=54842, avg=21795.16, stdev=11650.64
     lat (usec): min=330, max=55420, avg=21812.65, stdev=11644.68
    clat percentiles (usec):
     |  1.00th=[ 1156],  5.00th=[ 1450], 10.00th=[ 2024], 20.00th=[ 8979],
     | 30.00th=[21103], 40.00th=[21627], 50.00th=[22676], 60.00th=[23987],
     | 70.00th=[26346], 80.00th=[33817], 90.00th=[36439], 95.00th=[37487],
     | 99.00th=[41681], 99.50th=[44303], 99.90th=[48497], 99.95th=[50594],
     | 99.99th=[53740]
   bw (  KiB/s): min=21696, max=58489, per=99.78%, avg=23418.27, stdev=3498.39, samples=119
   iops        : min= 5424, max=14622, avg=5854.55, stdev=874.57, samples=119
  lat (usec)   : 500=0.01%, 750=0.03%, 1000=0.30%
  lat (msec)   : 2=9.54%, 4=7.04%, 10=3.64%, 20=6.83%, 50=72.56%
  lat (msec)   : 100=0.06%
  cpu          : usr=1.00%, sys=3.78%, ctx=8162, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,352172,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=22.9MiB/s (24.0MB/s), 22.9MiB/s-22.9MiB/s (24.0MB/s-24.0MB/s), io=1376MiB (1442MB), run=60017-60017msec

Disk stats (read/write):
  sdb: ios=0/159151, merge=0/212037, ticks=0/741529, in_queue=649820, util=99.97%
----------------------
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=74: Thu Jul 21 08:49:24 2022
  read: IOPS=23, BW=23.7MiB/s (24.9MB/s)(1554MiB/65447msec)
    slat (usec): min=12, max=425, avg=53.33, stdev=40.80
    clat (msec): min=13, max=15379, avg=5386.57, stdev=3122.42
     lat (msec): min=13, max=15379, avg=5386.63, stdev=3122.41
    clat percentiles (msec):
     |  1.00th=[   32],  5.00th=[ 1519], 10.00th=[ 1754], 20.00th=[ 2400],
     | 30.00th=[ 3037], 40.00th=[ 3910], 50.00th=[ 4933], 60.00th=[ 5940],
     | 70.00th=[ 7148], 80.00th=[ 8423], 90.00th=[ 9866], 95.00th=[10805],
     | 99.00th=[12416], 99.50th=[13758], 99.90th=[15100], 99.95th=[15368],
     | 99.99th=[15368]
   bw (  KiB/s): min=14336, max=56713, per=99.58%, avg=24212.34, stdev=3259.61, samples=120
   iops        : min=   14, max=   55, avg=23.64, stdev= 3.15, samples=120
  lat (msec)   : 20=0.32%, 50=1.09%, 100=0.06%, 250=0.19%, 500=0.39%
  lat (msec)   : 750=0.39%, 1000=0.39%, 2000=11.45%, >=2000=85.71%
  cpu          : usr=0.05%, sys=0.17%, ctx=1554, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1554,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=23.7MiB/s (24.9MB/s), 23.7MiB/s-23.7MiB/s (24.9MB/s-24.9MB/s), io=1554MiB (1629MB), run=65447-65447msec

Disk stats (read/write):
  sdb: ios=1549/3, merge=0/1, ticks=7986739/4953, in_queue=7990830, util=99.88%
----------------------
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=1022KiB/s][w=0 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=77: Thu Jul 21 08:50:29 2022
  write: IOPS=23, BW=23.7MiB/s (24.8MB/s)(1520MiB/64137msec); 0 zone resets
    slat (usec): min=26, max=1968.8k, avg=3404.27, stdev=73084.73
    clat (msec): min=1615, max=10769, avg=5396.69, stdev=1339.12
     lat (msec): min=1615, max=10769, avg=5400.10, stdev=1340.49
    clat percentiles (msec):
     |  1.00th=[ 2601],  5.00th=[ 4111], 10.00th=[ 4530], 20.00th=[ 4799],
     | 30.00th=[ 4933], 40.00th=[ 5134], 50.00th=[ 5269], 60.00th=[ 5470],
     | 70.00th=[ 5470], 80.00th=[ 5470], 90.00th=[ 6074], 95.00th=[ 8020],
     | 99.00th=[10268], 99.50th=[10268], 99.90th=[10805], 99.95th=[10805],
     | 99.99th=[10805]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=178304.00, stdev=98057.56, samples=16
   iops        : min=    2, max=  256, avg=174.12, stdev=95.76, samples=16
  lat (msec)   : 2000=0.07%, >=2000=99.93%
  cpu          : usr=0.06%, sys=0.06%, ctx=88, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.1%, 32=2.1%, >=64=95.9%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1520,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.7MiB/s (24.8MB/s), 23.7MiB/s-23.7MiB/s (24.8MB/s-24.8MB/s), io=1520MiB (1594MB), run=64137-64137msec

Disk stats (read/write):
  sdb: ios=0/1545, merge=0/15, ticks=0/4182606, in_queue=4181855, util=99.88%
```
