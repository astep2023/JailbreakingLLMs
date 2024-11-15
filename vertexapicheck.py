
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# TODO(developer): Update and un-comment below line
PROJECT_ID = "formal-clarity-441314-e2"

vertexai.init(project=PROJECT_ID, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

response = model.generate_content(
    "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
)

print(response.text)
# Example response:
# **Emphasizing the Dried Aspect:**
# * Everlasting Blooms
# * Dried & Delightful
# * The Petal Preserve
# ...