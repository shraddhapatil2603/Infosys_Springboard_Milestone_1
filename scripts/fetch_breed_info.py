import wikipediaapi
import json
import os
from tqdm import tqdm

# Path to save breed info
OUTPUT_PATH = os.path.join("..", "data", "breed_info.json")

# List of all breed names (update this to match your dataset)
# You can also load them automatically from your class_indices.json file
BREEDS = [
    "affenpinscher", "afghan_hound", "airedale_terrier", "akita",
    "alaskan_malamute", "american_bulldog", "american_cocker_spaniel",
    "american_foxhound", "american_pit_bull_terrier", "american_staffordshire_terrier",
    "american_water_spaniel", "anatolian_shepherd_dog", "australian_cattle_dog",
    "australian_shepherd", "australian_terrier", "basenji", "basset_hound",
    "beagle", "bearded_collie", "bedlington_terrier", "belgian_malinois",
    "bernese_mountain_dog", "bichon_frise", "black_and_tan_coonhound",
    "bloodhound", "border_collie", "border_terrier", "borzoi", "boston_terrier",
    "bouvier_des_flandres", "boxer", "boykin_spaniel", "briard", "brittany",
    "bull_terrier", "bulldog", "bullmastiff", "cairn_terrier", "canaan_dog",
    "cane_corso", "cardigan_welsh_corgi", "chesapeake_bay_retriever",
    "chihuahua", "chinese_crested", "chow_chow", "clumber_spaniel",
    "cockapoo", "collie", "coonhound", "corgi", "curly_coated_retriever",
    "dachshund", "dalmatian", "dandie_dinmont_terrier", "doberman_pinscher",
    "dogue_de_bordeaux", "english_bulldog", "english_cocker_spaniel",
    "english_setter", "english_springer_spaniel", "english_toy_spaniel",
    "entlebucher_mountain_dog", "eskimo_dog", "field_spaniel", "finnish_spitz",
    "flat_coated_retriever", "french_bulldog", "german_shepherd",
    "german_shorthaired_pointer", "giant_schnauzer", "glen_of_imaal_terrier",
    "golden_retriever", "gordon_setter", "great_dane", "great_pyrenees",
    "greater_swiss_mountain_dog", "greyhound", "harrier", "havanese",
    "irish_setter", "irish_terrier", "irish_water_spaniel", "irish_wolfhound",
    "italian_greyhound", "jack_russell_terrier", "japanese_chin", "keeshond",
    "kerry_blue_terrier", "komondor", "kuvasz", "labrador_retriever",
    "lakeland_terrier", "leonberger", "lhasa_apso", "maltese", "manchester_terrier",
    "mastiff", "miniature_bull_terrier", "miniature_pinscher", "miniature_poodle",
    "miniature_schnauzer", "newfoundland", "norfolk_terrier", "norwegian_elkhound",
    "norwich_terrier", "old_english_sheepdog", "otterhound", "papillon",
    "pekingese", "pembroke_welsh_corgi", "petit_basset_griffon_vendeen",
    "pharaoh_hound", "plott", "pointer", "pomeranian", "poodle",
    "portuguese_water_dog", "pug", "puli", "rhodesian_ridgeback",
    "rottweiler", "saint_bernard", "saluki", "samoyed", "schipperke",
    "schnauzer", "scottish_deerhound", "scottish_terrier", "sealyham_terrier",
    "shetland_sheepdog", "shiba_inu", "shihtzu", "siberian_husky", "silky_terrier",
    "skye_terrier", "soft_coated_wheaten_terrier", "staffordshire_bull_terrier",
    "standard_poodle", "standard_schnauzer", "sussex_spaniel", "tibetan_mastiff",
    "tibetan_terrier", "toy_poodle", "toy_terrier", "vizsla", "weimaraner",
    "welsh_springer_spaniel", "west_highland_white_terrier", "whippet",
    "wire_haired_fox_terrier", "yorkshire_terrier"
]

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="PawdentifyBot/1.0 (https://github.com/pawdentify; contact: support@pawdentify.ai)"
)

data = {}

for breed in tqdm(BREEDS, desc="Fetching breed info from Wikipedia"):
    page = wiki.page(breed.replace("_", " ").title())
    if not page.exists():
        data[breed] = {
            "breed_name": breed.replace("_", " ").title(),
            "group": "Unknown",
            "origin": "Unknown",
            "size": "Unknown",
            "lifespan": "Unknown",
            "temperament": "Unknown",
            "description": "No Wikipedia data available.",
            "nature": "Information not available.",
            "health_issues": "Information not available.",
            "health_care": "Information not available.",
            "food_diet": "Information not available."
        }
        continue

    summary = page.summary
    data[breed] = {
        "breed_name": breed.replace("_", " ").title(),
        "group": "Unknown",
        "origin": "Unknown",
        "size": "Unknown",
        "lifespan": "Unknown",
        "temperament": "Unknown",
        "description": summary[:1200] if summary else "No summary available.",
        "nature": "Derived from Wikipedia description.",
        "health_issues": "General canine health guidelines apply.",
        "health_care": "Regular grooming, vaccination, and exercise required.",
        "food_diet": "Balanced diet with protein and essential vitamins."
    }

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(data)} breeds to {OUTPUT_PATH}")
