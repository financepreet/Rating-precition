Section 1: Task 1 - Rating Prediction via Prompting

 1.1 Approach & Design Decisions
* This was a valuable project experience for me. I explored the Generative AI ($GenAI$) field extensively, and this project has added significant experience to my repertoire.
* At the start, I first designed the architecture for all working components, then proceeded with implementation and successfully completed it.
* For the API, I used $OpenAI$ models via $GroqCloud$, which are highly versatile and fast.
* I then performed prompt tuning through several iterations and achieved positive results.



1.2 Prompt Iterations
Three specific iterations were tested to assess performance gains:

* **Baseline (Zero-Shot):** Simple instruction defining the rating scale and structured $JSON$ format.
* **First Prompt:** I utilized a sample from the dataset to check if the model predicted star ratings correctly; I obtained positive results.
* **Second Prompt:** I designed this one myself to verify that the model was generating the correct star ratings. I also wanted to see how the model handled a positive review—the resulting rating and explanation were very close to my expectations.
* **Third Prompt:** I wrote a negative review using specific negative terms like "bad" and "worst" to confirm the model would assign a low star rating.

 1.3 Web Application
* Following positive feedback, I developed a $Streamlit$ project.
* I chose $Streamlit$ because it is user-friendly, enables rapid building, and provides strong graphical components. Given the limited timeline of only one day, I prioritized this over frameworks like $Flask$ or $FastAPI$, which might offer better documentation but require more development time.
