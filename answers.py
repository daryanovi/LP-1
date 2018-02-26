def get_answer():
	question=input("Введите вопрос: ")
	answers={"привет":"И тебе привет!", "как дела": "хорошо", "пока":"И тебе не хворать"}
	bot=answers[question.lower()]
	return bot
print(get_answer())