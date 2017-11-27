from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/classroom.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/classroom.courses ' \
         'https://www.googleapis.com/auth/classroom.courses.readonly ' \
         'https://www.googleapis.com/auth/classroom.coursework.me ' \
         'https://www.googleapis.com/auth/classroom.coursework.me.readonly ' \
         'https://www.googleapis.com/auth/classroom.coursework.students ' \
         'https://www.googleapis.com/auth/classroom.coursework.students.readonly ' \
         'https://www.googleapis.com/auth/classroom.profile.emails ' \
         'https://www.googleapis.com/auth/classroom.rosters ' \
         'https://www.googleapis.com/auth/classroom.rosters.readonly ' \
         'https://www.googleapis.com/auth/classroom.profile.photos'

CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Classroom API Python Quickstart'
print(SCOPES)


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'classroom.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def serviceObject():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('classroom', 'v1', http=http)
    return service


def createNewAssignment():
    service = serviceObject()

    courseWork = {
        'title': 'Ant 3',
        'description': 'Never ending ant assignments',
        'materials': [
            {'link': {'url': 'https://drive.google.com/open?id=1PgYhhCUzMr3gbZdvU-K0V_rD1oNC6nMLYLKJ5u7gAcw'}},
            {'link': {'url': 'http://google.com'}}
        ],
        'workType': 'ASSIGNMENT',
        'state': 'PUBLISHED',
    }
    courseWork = service.courses().courseWork().create(courseId='5358491732', body=courseWork).execute()
    # courseId = course.get('id')
    print('Assignment created with ID {0}'.format(courseWork.get('id')))

def main():
    """Shows basic usage of the Classroom API.

    Creates a Classroom API service object and prints the names of the first
    10 courses the user has access to.
    """
    service = serviceObject()
    option = 1

    courseResults = service.courses().list(pageSize=10).execute()
    courses = courseResults.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Your available courses are:')

        for course in courses:
            print(option,"    ", course['name'], '(id =', course['id'],')')
            option = option + 1

    getCourseRequired = input('\nPlease select the course you wish to check from the list above:\n')
    reqName = courses[int(getCourseRequired) - 1].get('name')
    reqId = courses[int(getCourseRequired)-1].get('id')
    print('You selected:\n', reqName, reqId,'\n')
    option = 1

    courseWorkResults = service.courses().courseWork().list(courseId=reqId).execute()
    print('### courseworkresults ###', courseWorkResults)
    assignments = courseWorkResults.get('courseWork',[])

    for assignment in assignments:
        print('The assignments in the chosen course are:')
        print(option, '     ', assignment['title'], '(id = ', assignment['id'], ')')
        option = option +1

    getCourseWorkRequired = input('\nPlease select the assignment you wish to check the status of:\n')
    reqCourseWorkTitle = assignments[int(getCourseWorkRequired)-1].get('title')
    reqCourseWorkId = assignments[int(getCourseWorkRequired)-1].get('id')
    print('You selected:\n', reqCourseWorkTitle, "(id = ", reqCourseWorkId, ")\n")

    studentSubmissionResults = service.courses().courseWork()\
        .studentSubmissions().list(courseId = reqId,
                                   courseWorkId = reqCourseWorkId).execute()

    print('### studentSubmissionResults ###', studentSubmissionResults)

    students = studentSubmissionResults.get('studentSubmissions', [])

    for student in students:
        studentId = service.userProfiles().get(userId = student['userId']).execute()
        studentEmail = studentId.get('emailAddress')
        assignmentState = student['state']
        print('The following students have completed the work:\n', studentEmail , assignmentState )
        if assignmentState == 'TURNED_IN':
            print('Creating new assignment for', studentEmail)
            createNewAssignment()
        else:
            print('No new assignments created')




if __name__ == '__main__':
    main()
