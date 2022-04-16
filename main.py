from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    print("1. Print all h5 tags: ")
    # Find first tag
    # courses_html_tags = soup.find('h5')
    courses_html_tags = soup.find_all('h5')
    print(courses_html_tags)
    print()

    print("2. Print Course Name: ")
    for course in courses_html_tags:
        print(course.text)

    print("3. Grab Price of each Course: ")
    course_cards = soup.find_all('div', class_='card')
    # Note class built-in keyword for python
    # where class_ points to the html file class element
    for course in course_cards:
        # print(course.h5)
        # print(course)
        course_name = course.h5.text  # Reminder why python is so powerful
        course_price = course.a.text.split()[-1]
        # Reminder why python is so powerful
        print(f'{course_name} costs {course_price}')
