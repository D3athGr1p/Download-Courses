- userID = `123`
- courseName = `ml-foundations`

- url = `https://www.coursera.org/api/guidedCourseSessionProgresses.v1?ids={userID}~{courseName}&fields=courseId,courseProgressState,currentWeekByUserProgress,endedAt,hasSessionModuleDeadlines,id,startedAt,weeks,onDemandCoursePresentGrades.v1`

- copy all the response from this url and open it in vs code.
- search and replace `true` with `""`.
- search and replace `false` with `""`.

- remove `,"paging":{},"linked":{}` at the and of the response

- store this link into variable = `link`

- find `courseID` and set it appropriate ID

- Now run this script `python main.py`



> Note HOW to find userID, courseName and courseID

- Login Into coursera website first

> For userID

- Press `F12` Key and you will find network tab is opened refresh the page and wait until all Containe is loaded Now press `ctrl+f` and paste `userId` and there is little refresh logo. do not refresh the page.

- You will find `userId` = `123456` copy this number and set it into `userID`.

> For courseName

- OpenCourse you want to download and copy the course link.

- `https://www.coursera.org/learn/ml-foundations/home/welcome`

- In this url `ml-foundations` is course name so set `courseName` = `ml-foundations`.

> For courseID

- Press `F12` Key and you will find network tab is opened refresh the page and wait until all Containe is loaded Now press `ctrl+f` and paste `courseid` and there is little refresh logo. do not refresh the page.

- You will find `courseid` = `123456` copy this number and set it into `courseID`.
