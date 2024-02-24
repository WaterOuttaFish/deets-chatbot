from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

#loading the model
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

#pipe!
pipe = pipeline('question-answering', model=model, tokenizer=tokenizer)

#info the ai uses to answer the questions
context = """
Offred is a Handmaid in the Republic of Gilead, a totalitarian and theocratic state that has replaced the United States of America. Because of dangerously low reproduction rates, Handmaids are assigned to bear children for elite couples that have trouble conceiving. Offred serves the Commander and his wife, Serena Joy, a former gospel singer and advocate for “traditional values.” Offred is not the narrator’s real name—Handmaid names consist of the word “of” followed by the name of the Handmaid’s Commander. Every month, when Offred is at the right point in her menstrual cycle, she must have ritualized sex with the Commander while Serena sits behind her, holding her hands. Offred’s freedom, like the freedom of all women, is completely restricted. She can leave the house only on shopping trips, the door to her room cannot be completely shut, and the Eyes, Gilead’s secret police force, watch her every public move.
As Offred tells the story of her daily life, she frequently slips into flashbacks, from which the reader can reconstruct the events leading up to the beginning of the novel. In the old world, before Gilead, Offred had an affair with Luke, a married man. Luke divorced his wife and married Offred, and they had a child together. Offred’s mother was a single mother and feminist activist. Offred’s best friend, Moira, was fiercely independent. The architects of Gilead began their rise to power in an age of readily available pornography, prostitution, and violence against women—when pollution and chemical spills led to declining fertility rates. Using the military, they assassinated the president and members of Congress and launched a coup, claiming that they were taking power temporarily. They cracked down on women’s rights, forbidding women to hold property or jobs. Offred and Luke took their daughter and attempted to flee across the border into Canada, but they were caught and separated from one another, and Offred has seen neither her husband nor her daughter since.
After her capture, Offred’s marriage was voided (because Luke had been divorced), and she was sent to the Rachel and Leah Re-education Center, called the Red Center by its inhabitants. At the center, women were indoctrinated into Gilead’s ideology in preparation for becoming Handmaids. Aunt Lydia supervised the women, giving speeches extolling Gilead’s beliefs that women should be subservient to men and solely concerned with bearing children. Aunt Lydia also argued that such a social order ultimately offers women more respect and safety than the old, pre-Gilead society offered them. Moira is brought to the Red Center, but she escapes, and Offred does not know what becomes of her.
"""

#user interaction - input
questions = input("Please input your question:\n")

#answers question + computer output 
result = pipe(question=questions, context=context)
print(result['answer'].capitalize())

#idk what im supposed to put as comments ngl