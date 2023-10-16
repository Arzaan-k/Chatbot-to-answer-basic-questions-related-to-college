from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('College Bot')

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "help us",
    "I can provide you information and details related to our collage M.H Saboo Siddik engineering collage ",
    "hii",
    "Hello",
    "What is your name",
    "I am a Chatbot of M.H Saboo Siddik Collage, you can consider my name as MHSSCE.",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Where is saboo siddik college is located ",
    "The address of Saboo Siddik College of Engineering is 8, Shepherd Rd, Agripada, Mumbai, Maharashtra 400011.",
    "When was Saboo Siddik College of Engineering established",
    "Saboo Siddik College of Engineering was established in 1936.",
    "Is Saboo Siddik College of Engineering affiliated to any university",
    "Yes, Saboo Siddik College of Engineering is affiliated to the University of Mumbai.",
    "What are the courses offered ",
    "Saboo Siddik College of Engineering offers undergraduate programs in Bachelor of Engineering (B.E.) in various disciplines such as Mechanical, Electronics & Telecommunication, Computer, and Information Technology. The college also offers postgraduate courses in Master of Engineering (M.E.) in various specializations.",
    "What is the admission process ",
    "The admission process at Saboo Siddik College of Engineering is based on the scores obtained in the entrance exam conducted by the Government of Maharashtra. For postgraduate courses, the admission is based on the candidate's performance in the qualifying examination and entrance exam.",
    "What are the facilities  ",
    "Saboo Siddik College of Engineering offers facilities such as well-equipped classrooms, computer labs, a well-stocked library, laboratories, sports facilities, hostel, canteen, transportation, medical facilities, and a placement cell for providing placement opportunities to students.",
    "fee structure",
    "The fee structure at Saboo Siddik College of Engineering varies for different courses. You can visit the official website of the college for more details. link- https://www.mhssce.ac.in/",
    "When is my exams",
    "According to the Mumbai University exams for current semester starts from 9th May 2023 till 23rd May 2023",
    "When is our practical exams?",
    "It starts from 2nd May 2023",
    "How old is our college?",
    "150 years old",
    "What are the extracurricular activities available for students at Saboo Siddik College?",
    "Saboo Siddik College of Engineering encourages its students to participate in various extracurricular activities such as sports, cultural events, technical fests, and more. The college has several clubs and associations that organize various activities and events throughout the year.",
    "What are the admission requirements ",
    "The admission requirements for Saboo Siddik College of Engineering include passing the HSC (12th) examination or its equivalent with Physics, Chemistry, and Mathematics as compulsory subjects. Additionally, candidates must qualify for the MH-CET or JEE Main entrance exams and secure a valid score.",
    "How do I apply for admission to Saboo Siddik College?",
    "Candidates can apply for admission to Saboo Siddik College of Engineering through the official website or offline mode by obtaining the application form from the college admission office. The candidates must fill in the necessary details and submit the form along with the required documents and application fee.",
    "Can you tell me about the faculty ",
    "Saboo Siddik College of Engineering has a team of highly qualified and experienced faculty members who are experts in their respective fields. The faculty members are dedicated to imparting quality education and providing guidance to the students.",
    "tell me about placement  ",
    "Saboo Siddik College of Engineering has a dedicated placement cell that offers placement opportunities to its students. The cell has a good track record of placing its students in reputed companies such as TCS, Wipro, Infosys, Capgemini, and many more.",
    "Who is HOD of IT",
    "Prof. Shrinidhi Gindi is the HOD of IT",
    "located , address, location",
    "The address of Saboo Siddik College of Engineering is 8, Shepherd Rd, Agripada, Mumbai, Maharashtra 400011.",
    "Contact?",
    "+91 22 23012922 - contact number and aimhssce@gmail.com - mail id",
    "president ",
    "Dr. Zahir I. Kazi is the president of college",
    "Who builts you ",
    "Faayeez and Arzan",
    "Subjects ",
    "For sem 4 : 1) mathematics 4 , 2) automata theory , 3) computer networks and network design , 4) computer organisation and architecture , 5) Operating systems",
    "under who's guidance you are created  ",
    "I am created under the guidance of DR. IRFAN LANDGE sir ",
    "names of group members  ",
    "Our group members are Faayeez ,Arzan ,Shams ,Sameed ",
    "Communities?",
    "Our college has several student chapters and communities such as the ACM , IEEE Student Branch, IETE Student Forum, CSI Student Branch, Codechef Campus Chapter, Robotics Club, and Entrepreneurship Development Cell (EDC).",
    # "",
    # "",
    # "",
    # "",

]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 