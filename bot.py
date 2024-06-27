from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ContactInfoAdapter(LogicAdapter):
    def can_process(self, statement):
        keywords = ['contact', 'reach', 'email', 'phone']
        return any(keyword in statement.text.lower() for keyword in keywords)

    def process(self, statement, additional_response_selection_parameters=None):
        response_text = "You can contact us via email at info@educonsult.com or call us at (123) 456-7890."
        response = Statement(text=response_text)
        response.confidence = 1
        return response

class ServicesAdapter(LogicAdapter):
    def can_process(self, statement):
        keywords = ['services', 'offer', 'provide']
        return any(keyword in statement.text.lower() for keyword in keywords)

    def process(self, statement, additional_response_selection_parameters=None):
        response_text = "We offer educational consultancy services including admissions guidance, career counseling, and course selection advice."
        response = Statement(text=response_text)
        response.confidence = 1
        return response

# Define your chatbot with custom logic adapters
chatbot = ChatBot(
    "EduConsult",
    logic_adapters=[
        'bot.ContactInfoAdapter',
        'bot.ServicesAdapter',
        'chatterbot.logic.BestMatch'  # Fallback to BestMatch if no custom adapter matches
    ]
)

trainer = ListTrainer(chatbot)

# Training data
conversations = [
    ["Hi", "Hello! How can I help you today?"],
    ["Hello", "Hi there! How can I assist you?"],
    ["What services do you offer?", "We offer educational consultancy services including admissions guidance, career counseling, and course selection advice."],
    ["Can you help with university applications?", "Yes, we can assist you with the entire university application process including selecting universities, preparing application materials, and interview preparation."],
    ["What are the best universities for engineering?", "Some of the top universities for engineering include MIT, Stanford, UC Berkeley, and Cambridge."],
    ["How do I prepare for a university interview?", "To prepare for a university interview, you should research the university, practice common interview questions, and be ready to discuss your experiences and goals."],
    ["Do you offer career counseling?", "Yes, we offer career counseling services to help you choose the right career path and prepare for your future profession."],
    ["How can I improve my chances of getting a scholarship?", "To improve your chances of getting a scholarship, maintain a high GPA, participate in extracurricular activities, and prepare a strong application with a compelling personal statement."],
    ["How can I contact you?", "You can contact us via email at info@educonsult.com or call us at (123) 456-7890."],
    ["What documents are required for a university application?", "Commonly required documents include transcripts, letters of recommendation, a personal statement, and standardized test scores."],
    ["Can you help with visa applications?", "Yes, we provide assistance with the student visa application process, including document preparation and interview coaching."],
    ["What are the deadlines for university applications?", "Application deadlines vary by university and program. It's important to check the specific deadlines for each university you are interested in."],
    ["Do you offer test preparation services?", "Yes, we offer test preparation services for exams such as the SAT, ACT, GRE, and TOEFL."],
    ["How do I choose the right course for me?", "We can help you assess your interests and strengths, and provide guidance on choosing a course that aligns with your career goals."],
    ["What is the application process for international students?", "The application process for international students typically includes submitting an online application, providing academic and financial documents, and meeting language proficiency requirements."],
]

# Train the chatbot with the refined data
for conversation in conversations:
    trainer.train(conversation)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(f"🎓 {response}")
