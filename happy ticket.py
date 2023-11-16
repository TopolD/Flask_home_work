# from multiprocessing import Pool
#
# def is_lucky_ticket(ticket):
#     first_half = ticket[:len(ticket)//2]
#     second_half = ticket[len(ticket)//2:]
#     return sum(map(int, first_half)) == sum(map(int, second_half))
#
# def count_lucky_tickets(start, end):
#     count = 0
#     for ticket in range(start, end + 1):
#         ticket_str = str(ticket).zfill(10)
#         if is_lucky_ticket(ticket_str):
#             count += 1
#     return count
#
# def parallel_count(start, end, num_processes=4):
#     pool = Pool(processes=num_processes)
#     chunk_size = (end - start + 1) // num_processes
#     ranges = [(i, i + chunk_size - 1) for i in range(start, end + 1, chunk_size)]
#     results = pool.starmap(count_lucky_tickets, ranges)
#     pool.close()
#     pool.join()
#     return sum(results)
#
# if __name__ == "__main__":
#     start_range = 0
#     end_range = 100000
#     num_processes = 4
#
#     lucky_tickets_count = parallel_count(start_range, end_range, num_processes)
#
#     print(f"Кількість щасливих білетів в діапазоні {start_range}-{end_range}: {lucky_tickets_count}")


import re

text = "1984, 245, 1845, 2019, 2000, 1987, 2250, 2301, 2402"
pattern = r'\b(?:19\d\d|20(?:[01]\d|200|300))\b'
matches = re.findall(pattern, text)

print(matches)
