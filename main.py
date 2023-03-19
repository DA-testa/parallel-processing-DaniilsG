def parallel_processing(i, j, data):

    output = []
    finish_time = [0] * i

    for i, job_time in enumerate(data):

        min_finish_time = min(finish_time)

        min_thread = finish_time.index(min_finish_time)

        output.append((min_thread, min_finish_time))
        
        finish_time[min_thread] += job_time

    return output

def main():

    i, j = map(int, input().split())

    data = list(map(int, input().split()))


    result = parallel_processing(i, j, data)

    for a, b in result:

        print(a,b)

if __name__ == "__main__":
    main()