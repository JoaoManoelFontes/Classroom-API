from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import flow as Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
    "https://www.googleapis.com/auth/classroom.courses.readonly",
]


def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("src/token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file(
            # 'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)

            flow = Flow.InstalledAppFlow.from_client_secrets_file(
                "src/credentials.json", SCOPES
            )
            dic = flow.run_local_server(port=0)
            print(dic["url"])
            dic["server"].timeout = None
            dic["server"].handle_request()
            authorization_response = dic["wsgi"].last_request_uri.replace(
                "http", "https"
            )
            flow.fetch_token(authorization_response=authorization_response)
            dic["server"].server_close()
            creds = flow.credentials

    try:
        service = build("classroom", "v1", credentials=creds)

        # Call the Classroom API
        results = service.courses().list(pageSize=15).execute()
        # test = service.courses().courseWork().list(courseId='600044699098').execute()
        # print(test['courseWork'][0])
        # test = service.courses().list(courseId='600044699098').execute()
        # print(test)
        courses = results.get("courses", [])

        if not courses:
            print("No courses found.")
            return
        # Prints the names of the first 10 courses.
        print("Courses:")
        for i in range(2):
            print("--------- " + courses[i]["name"] + " ---------")
            print("------- course infos -------")
            print(courses[i])
            courseWork = (
                service.courses().courseWork().list(courseId=courses[i]["id"]).execute()
            )
            if "courseWork" in courseWork:
                print("------- tasks infos -------")
                for tasks in courseWork["courseWork"]:
                    print("-------" + tasks["title"] + " -------")
                    print("------- student submissions -------")
                    studentSubmission = (
                        service.courses()
                        .courseWork()
                        .studentSubmissions()
                        .list(courseId=courses[i]["id"], courseWorkId=tasks["id"])
                        .execute()
                    )
                    print(studentSubmission)
                    print("-------------------------")
            else:
                print("No tasks found.")

        if os.path.exists("src/token.json"):
            os.remove("src/token.json")
            print("token.json removed")

    except HttpError as error:
        print("An error occurred: %s" % error)


if __name__ == "__main__":
    main()

# # api classroom
# # https://googleapis.github.io/google-api-python-client/docs/dyn/classroom_v1.html
# # https://www.any-api.com/googleapis_com/classroom/docs/courses/classroom_courses_courseWork_list

# # api scopes
# # https://developers.google.com/resources/api-libraries/documentation/classroom/v1/cpp/latest/classgoogle__classroom__api_1_1ClassroomService_1_1SCOPES.html
