import os
from google import genai


def get_response(user_input:str):
    key = os.environ.get("API_KEY")
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="""Background for this professor: His name is Kevin Lin, he teaches CSE373 which is a non major
                    computer science course covering data structures and algorithms so no computer science major 
                    will be taking this course. Refer to him as Kevin.
                    Response:
                    Write ONLY a short rating of around 25 to 50 words summarizing the user input on Kevin
                    in a way that would look normal being posted on a ratings board. If there is none then
                    write ONLY the response of same length talking about lack of syllabus, unclear grading, biased
                    and egotistical behavior, and overall lack of communication. Do not include any portion of a
                    response from you as an ai. Do not include ANYTHING besides the text that will be posted to the
                    ratings board such as a header or label. Just the text.
                    User input:""" + user_input
    )
    return response.text