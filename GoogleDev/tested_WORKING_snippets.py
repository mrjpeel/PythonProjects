
print('CREATING COURSE')
course = {
    'name': '10th Grade Biology',
    'section': 'Period 2',
    'descriptionHeading': 'Welcome to 10th Grade Biology',
    'description': """We'll be learning about about the structure of living
                 creatures from a combination of textbooks, guest
                 lectures, and lab work. Expect to be excited!""",
    'room': '301',
    'ownerId': 'me',
    'courseState': 'PROVISIONED'
}
course = service.courses().create(body=course).execute()
print('Course created: {0} ({1})'.format(course.get('name'), course.get('id')))


print('CREATING ASSIGNMENT')
courseWork = {
    'title': 'Ant 2',
    'description': 'More Ants',
    'materials': [
        {'link': {'url': 'http://bbc.co.uk'}},
        {'link': {'url': 'http://google.com'}}
    ],
    'workType': 'ASSIGNMENT',
    'state': 'DRAFT',
}
courseWork = service.courses().courseWork().create(courseId='5358491732', body=courseWork).execute()
courseId = course.get('id')
print('Assignment created with ID {0}'.format(courseWork.get('id')))
