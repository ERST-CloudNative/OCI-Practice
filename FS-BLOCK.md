



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
