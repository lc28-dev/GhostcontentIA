import openai
import os

def generate_social_bundle(business_name, industry, tone, goal):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"Crée un post pour {business_name} dans le secteur {industry}."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except:
        return "Erreur : Clé API manquante ou invalide."
