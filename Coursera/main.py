import json

userID = '123'
courseName = 'ml-foundations'

# f'https://www.coursera.org/api/guidedCourseSessionProgresses.v1?ids={userID}~{courseName}&fields=courseId,courseProgressState,currentWeekByUserProgress,endedAt,hasSessionModuleDeadlines,id,startedAt,weeks,onDemandCoursePresentGrades.v1'


link = "ABCSomething"



zero = link["elements"][0]

def everyWeek():
	count = 0
	for _ in range(len(zero["weeks"])):
		fetchID(count ,zero["weeks"][_])
		count += 1

weeks = {}

def fetchID(week, links):
	link = []
	modules = links["modules"][0]
	items = modules["items"]
	for _ in items:
		link.append(_["id"])
	weeks[week] = link


everyWeek()

# Done with fetching all the lecture ID from all the weeks

# Now start with fetching the Link for all the lecture mp4 file

courseID = 'qi9mnkIJEeWC4g7VhG4bTQ'

def fetchMP4URL(ID):
	return f'https://www.coursera.org/api/onDemandLectureVideos.v1/{courseID}~{ID}?includes=video&fields=onDemandVideos.v1(sources%2Csubtitles%2CsubtitlesVtt%2CsubtitlesTxt)'

# def fetchDOCURL(ID):
# 	return f'https://www.coursera.org/api/onDemandSupplements.v1/qi9mnkIJEeWC4g7VhG4bTQ~{ID}?includes=asset&fields=openCourseAssets.v1(typeName)%2CopenCourseAssets.v1(definition)'



def fetchWeekIDs(weekNo):
	return weeks[weekNo]

weeksURL = []



def startFetching():
	count = 0
	weekURL = {}
	for _ in range(len(weeks)):
		weekIDs = fetchWeekIDs(_)
		f = open("urls.txt", "a")
		for __ in range(len(weekIDs)):
			weeklyURL = []
			weekURL[__] = fetchMP4URL(weekIDs[__])
			f.write(f'{weekURL[__]}\n')
			print(weekURL[__])
		f.write(f"Week No {_} \n")
		print("weekDone \n")
		f.close()





startFetching()

