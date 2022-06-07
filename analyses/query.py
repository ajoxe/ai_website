def search(cont):
	question = "What is climate change?"
	answer = "Sorry, we were not able to find an answer"
	links = ["", ""]
	if cont.lower()  == question.lower():
		answer = "a systematic change in the long-term state of the atmosphere over multiple decades or longer."
		links = ["https://www.climatehubs.usda.gov/climate-change-101", "http://arxiv.org/abs/1111.0337v1"]
	return answer, links
