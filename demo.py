from download_image import download_image
from crawl_titles import get_titles_on_web
from natural_language_processing import get_name_of_object_in_image

if __name__ == "__main__":
	filename= "test.jpg"
	titles  = get_titles_on_web(filename)
	title   = get_name_of_object_in_image(titles)

	try:
		download_image(title)
	except Exception:
		print("Could not crawl")