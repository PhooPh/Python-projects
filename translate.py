translate_to_burmese={
       "Hello":"Mingalarpar",
       "Nice to meet you":"twae ya tr wan thr pr tl",
       "How are you":"Nay Kaung Lar",
       "What is your name ?":"Min Na ml bl loh khaw tha ll",
       "I'm good":"Ngr a sin pyay pr tl",
       "Mingalarpar":"Hello",
       "twae ya tr wan thr pr tl":"Nice to meet you",
       "Nay Kaung Lar":"How are you",
       "Min Na ml bl loh khaw tha ll":"What is your name ?",
       "Ngr a sin pyay pr tl":"I'm good",
}
user_que=input("Enter Your Questions : ")
for i in translate_to_burmese:
       if user_que == i:
              translated=translate_to_burmese.get(user_que)

              print(translated)