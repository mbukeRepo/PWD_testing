import subprocess
import timeit

def crack_password():
    password = [0, 0, 0, 0, 0, 0, 0, 0]
    trials = 100
    i_time = []
    for i in range(8):
        for j in range(0, 10):
            password[i] = j
            new_pwd = "".join(password)
            i_time = timeit.repeat(stmt='check_password(x)',
                                   setup=f'x={new_pwd!r})',
                                   globals=globals(),
                                   number=trials,
                                   repeat=10)
        print(max(i_time))

def check_password(inputdata):
    inputdata = bytes(inputdata, 'utf-8')
    process=subprocess.Popen(['./pin_checker'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdoutdata,stderrdata=process.communicate(input=inputdata)
    print(stdoutdata.decode('utf-8'), inputdata)
    return 'Access denied' not in stdoutdata.decode('utf-8')


if __name__ == "__main__":
    crack_password()
