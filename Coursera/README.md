- userID = `123`
- courseName = `ml-foundations`

- url = `https://www.coursera.org/api/guidedCourseSessionProgresses.v1?ids={userID}~{courseName}&fields=courseId,courseProgressState,currentWeekByUserProgress,endedAt,hasSessionModuleDeadlines,id,startedAt,weeks,onDemandCoursePresentGrades.v1`

- serach this entire `url` on google.

- copy all the response from this url and open it in vs code.
- search and replace `true` with `""`.
- search and replace `false` with `""`.

- remove `,"paging":{},"linked":{}` at the end of the response

- store this link into variable = `link`

- find `courseID` and set it appropriate ID

- Now run this script `python main.py`



# Note HOW to find userID, courseName and courseID

- Login Into coursera website first

> For userID

- Press `F12` Key and you will find network tab is opened refresh the page and wait until all Containe is loaded Now press `ctrl+f` and paste `userId` and there is little refresh logo prees that do not refresh the page.

- You will find `userId` = `123456` copy this number and set it into `userID`.

> For courseName

- OpenCourse you want to download and copy the course link.

- `https://www.coursera.org/learn/ml-foundations/home/welcome`

- In this url `ml-foundations` is course name so set `courseName` = `ml-foundations`.

> For courseID

- Press `F12` Key and you will find network tab is opened refresh the page and wait until all Containe is loaded Now press `ctrl+f` and paste `courseid` and there is little refresh logo prees that do not refresh the page.

- You will find `courseid` = `123456` copy this number and set it into `courseID`.


# Note : At then end of the script will print some links on termianl.

- Now this copy all the links and save into the some files.

- Now there will be some problems.

- If you want to watch only videos then its all good but if you want read docs then you have to do some manual works.

- copy link and paste into web if there is some problme into response then remeber this is doc URL not video url so you have to change url first.

```javascript
https://www.coursera.org/api/onDemandSupplements.v1/{courseID}~{ID}?includes=asset&fields=openCourseAssets.v1(typeName)%2CopenCourseAssets.v1(definition)

change the courseID and lectureid and paste into the web and you are good to go.
```