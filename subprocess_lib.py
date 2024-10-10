import subprocess



comand = ['ping', '127.0.0.1']



subproccess_ =  subprocess.run(
    comand,
    shell= True,
    capture_output= True,
    text= True,
    encoding='cp437'
    
)

convergion = str(subproccess_).split('\\n')
[print(i) for i in convergion]