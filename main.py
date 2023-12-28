import atexit

import concurrent.futures

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def is_similar_match(search_query, results):
    # Check if there is at least one similar match in the results
    return any(search_query.lower() in result.lower() for result in results)


def get_similar_match(search_query, results):
    # Find and return the first similar match in the results
    for result in results:
        if search_query.lower() in result.lower():
            return result
    return None


def perform_search_and_check_flixwave(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://flixwave.to/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        # Find all img elements with class "lazyload" on the search results page
        img_elements = driver.find_elements(By.CSS_SELECTOR, "img.lazyload")

        # Check if the search term is in the alt attribute of any img element
        results_with_search_term = [
            img.get_attribute("alt")
            for img in img_elements
            if img.get_attribute("alt")
            and search_query.lower() in img.get_attribute("alt").lower()
        ]

        # Close the browser window
        driver.quit()

        return is_similar_match(
            search_query, results_with_search_term
        ), get_similar_match(search_query, results_with_search_term)

    except Exception as e:
        print(f"An error occurred for Flixwave: {e}")
        return False, None


def perform_search_and_check_flixhq(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://flixhq.id/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div/div[2]/div/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        # Find all <a> elements with class "m-title"
        title_elements = driver.find_elements(By.CSS_SELECTOR, "a.m-title")

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for flixhq: {e}")
        return False, None


def perform_search_and_check_fmovies(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://fmovies.llc/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[4]/div/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name a",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for fmovies: {e}")
        return False, None


def perform_search_and_check_nites(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://ww4.nites.is/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/center/div/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        # Find movie title elements using the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR, ".post.movies .entry-title"
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for nites: {e}")
        return False, None


def perform_search_and_check_movies123(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://movies123.la/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/input")

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        # Find movie title elements using the provided CSS selector
        title_elements = driver.find_elements(By.CSS_SELECTOR, ".text-light")

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for movies123: {e}")
        return False, None


def perform_search_and_check_movie4kto(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://movie4kto.net/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[3]/div[1]/div/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail-fix .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for movie4kto: {e}")
        return False, None


def perform_search_and_check_movies2watch(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://movies2watch.to/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div/form/input"
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for movies2watch: {e}")
        return False, None


def perform_search_and_check_serieshd(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://serieshd.watch/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div/form/input",
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for serieshd: {e}")
        return False, None


def perform_search_and_check_worthful(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://www.worthful.info")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[4]/div[1]/div/div[3]/div[1]/div/form/input",
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for worthful: {e}")
        return False, None


def perform_search_and_check_watchfreemovies(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://watchfreemovi.es/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div/form/input",
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for watchfreemovies: {e}")
        return False, None


def perform_search_and_check_freemoviesfull(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://freemoviesfull.cc")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/div[2]/div/div/div[3]/div/form/input",
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for freemoviesfull: {e}")
        return False, None


def perform_search_and_check_favhd(search_query):
    try:
        # Disable JavaScript by setting the property to undefined
        chrome_options = Options()

        # Open an automated Chrome instance as a driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get("https://favhd.net/")  # Replace with the actual website URL

        # Find the search box element by its XPath
        search_box = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input",
        )

        # Input the query into the search box
        search_box.send_keys(search_query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (you might need to adjust the time)
        driver.implicitly_wait(5)

        prefs = {"profile.managed_default_content_settings.javascript": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Find all <a> elements that match the provided CSS selector
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".flw-item .film-detail .film-name",
        )

        # Extract titles from the <a> elements
        titles = [title.text for title in title_elements]

        # Close the browser window
        driver.quit()

        return is_similar_match(search_query, titles), get_similar_match(
            search_query, titles
        )

    except Exception as e:
        print(f"An error occurred for favhd: {e}")
        return False, None


def prompt_user_for_website():
    print("Choose a website:")
    print("1. Flixwave")
    print("2. Flixhq")
    print("3. Fmovies")
    print("4. nites")
    print("5. movies123")
    print("6. movie4kto")
    print("7. movies2watch")
    print("8. serieshd")
    print("9. worthful")
    print("10. watchfreemovies")
    print("11. freemoviesfull")
    print("12. favhd")

    choice = input("Enter the number of the website you want to use: ")

    if choice == "1":
        return "https://flixwave.to/", "/html/body/div[1]/header/div[1]/form/input"
    elif choice == "2":
        return (
            "https://flixhq.id/",
            "/html/body/div[1]/header/div/div[2]/div/form/input",
        )
    elif choice == "3":
        return (
            "https://fmovies.llc/",
            "/html/body/div[1]/div[4]/div[1]/div/div[4]/div/form/input",
        )
    elif choice == "4":
        return "https://ww4.nites.is/", "/html/body/div[1]/div[2]/center/div/form/input"
    elif choice == "5":
        return "https://movies123.la/", "/html/body/main/div/div[1]/input"
    elif choice == "6":
        return (
            "https://movie4kto.net/",
            "/html/body/div[1]/div[4]/div[1]/div/div[3]/div[1]/div/form/input",
        )
    elif choice == "7":
        return (
            "https://movies2watch.to/",
            "/html/body/div[1]/div[4]/div/div[2]/div/form/input",
        )
    elif choice == "8":
        return (
            "https://serieshd.watch/",
            "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div/form/input",
        )
    elif choice == "9":
        return (
            "https://www.worthful.info",
            "/html/body/div[1]/div[4]/div[1]/div/div[3]/div[1]/div/form/input",
        )
    elif choice == "10":
        return (
            "https://watchfreemovi.es/",
            "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div/form/input",
        )
    elif choice == "11":
        return (
            "https://freemoviesfull.cc",
            "/html/body/div/div[2]/div[2]/div/div/div[3]/div/form/input",
        )
    elif choice == "12":
        return (
            "https://favhd.net/",
            "/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input",
        )
    else:
        print("Invalid choice. Exiting.")
        exit()


def perform_search_and_open_website(search_query, website_url, search_box_xpath):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the tasks to the ThreadPoolExecutor
            future1 = executor.submit(
                search_using_image_tags, search_query, website_url, search_box_xpath
            )
            future2 = executor.submit(
                search_using_links, search_query, website_url, search_box_xpath
            )
            future3 = executor.submit(
                search_using_javascript, search_query, website_url, search_box_xpath
            )
            future4 = executor.submit(search)

            # Wait for all tasks to complete
            concurrent.futures.wait([future1, future2, future3, future4])

            # Retrieve the result from the first completed task (if any)
            for future in concurrent.futures.as_completed(
                [future1, future2, future3, future4]
            ):
                result = future.result()
                if result is not None:
                    return result

    except Exception as e:
        print(f"An error occurred: {e}")


def search_using_image_tags(search_query, website_url, search_box_xpath):
    # Disable JavaScript by setting the property to undefined
    chrome_options = Options()
    prefs = {"profile.managed_default_content_settings.javascript": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Open an automated Chrome instance as a driver
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    # Open the website in the browser
    driver.get(website_url)

    # Find the search box element by its XPath
    search_box = driver.find_element(By.XPATH, search_box_xpath)

    # Input the query into the search box
    search_box.send_keys(search_query)

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load (you might need to adjust the time)
    driver.implicitly_wait(5)

    try:
        film_elements = driver.find_elements(By.TAG_NAME, "img")

        for film_element in film_elements:
            if search_query.lower() in film_element.get_attribute("alt").lower():
                film_element.click()
                film_url = driver.current_url
                print(f"URL for the film: {film_url}")
                atexit.register(driver.quit)
                return driver

    except Exception as e:
        print(f"An error occurred in search_using_image_tags: {e}")
        return None


def search_using_links(search_query, website_url, search_box_xpath):
    # Disable JavaScript by setting the property to undefined
    chrome_options = Options()
    prefs = {"profile.managed_default_content_settings.javascript": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Open an automated Chrome instance as a driver
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    # Open the website in the browser
    driver.get(website_url)

    # Find the search box element by its XPath
    search_box = driver.find_element(By.XPATH, search_box_xpath)

    # Input the query into the search box
    search_box.send_keys(search_query)

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load (you might need to adjust the time)
    driver.implicitly_wait(5)

    try:
        # If no film is found using image tags, try searching using link (a tag)
        film_links = driver.find_elements(
            By.CSS_SELECTOR, "a"
        )  # Customize this based on your page structure

        for film_link in film_links:
            if search_query.lower() in film_link.text.lower():
                # Click on the link element
                film_link.click()

                # Grab the current URL from the address bar
                film_url = driver.current_url

                # Print the URL to the console
                print(f"URL for the film: {film_url}")

                # Register a function to close the browser when the program exits
                atexit.register(driver.quit)

                # This line ensures that the program does not wait for the browser to close
                return driver

    except:
        # If no film is found using the link (a tag), try searching using the specified CSS selector
        film_link = driver.find_element(
            By.CSS_SELECTOR, ".lnk-blk:after, .lnk-blk-a > a:after"
        )

        if search_query.lower() in film_link.text.lower():
            film_link.click()

            # Grab the current URL from the address bar
            film_url = driver.current_url

            # Print the URL to the console
            print(f"URL for the film: {film_url}")

            # Register a function to close the browser when the program exits
            atexit.register(driver.quit)

            # This line ensures that the program does not wait for the browser to close
            return driver


def search_using_javascript(search_query, website_url, search_box_xpath):
    chrome_options = Options()

    # Open an automated Chrome instance as a driver
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    # Open the website in the browser
    driver.get(website_url)

    # Find the search box element by its XPath
    search_box = driver.find_element(By.XPATH, search_box_xpath)

    # Input the query into the search box
    search_box.send_keys(search_query)

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load (you might need to adjust the time)
    driver.implicitly_wait(5)

    try:
        # If no film is found using the link (a tag), try searching using the specified CSS selector
        film_link = driver.find_element(By.CSS_SELECTOR, "a")
        if search_query.lower() in film_link.text.lower():
            film_link.click()

            # Grab the current URL from the address bar
            film_url = driver.current_url

            # Print the URL to the console
            print(f"URL for the film: {film_url}")

            # Register a function to close the browser when the program exits
            atexit.register(driver.quit)

            # This line ensures that the program does not wait for the browser to close
            return driver
    except:
        # If no film is found using image or link, try searching using the specified XPath
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".film_list .film_list-wrap .flw-item .film-detail .film-name a",
        )

        for title_element in title_elements:
            if search_query.lower() in title_element.text.lower():
                # Click on the title element
                title_element.click()

                # Grab the current URL from the address bar
                film_url = driver.current_url

                # Print the URL to the console
                print(f"URL for the film: {film_url}")

                # Register a function to close the browser when the program exits
                atexit.register(driver.quit)

                # This line ensures that the program does not wait for the browser to close
                return driver


def search():
    # Disable JavaScript by setting the property to undefined
    chrome_options = Options()
    prefs = {"profile.managed_default_content_settings.javascript": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Open an automated Chrome instance as a driver
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    # Open the website in the browser
    driver.get(website_url)

    # Find the search box element by its XPath
    search_box = driver.find_element(By.XPATH, search_box_xpath)

    # Input the query into the search box
    search_box.send_keys(search_query)

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load (you might need to adjust the time)
    driver.implicitly_wait(5)

    # If no film is found, print the current URL
    current_url = driver.current_url
    print(f"Website URL: {current_url}")

    # Register a function to close the browser when the program exits
    atexit.register(driver.quit)

    # This line ensures that the program does not wait for the browser to close
    return driver


# Example usage
search_query = input("film: ")

# Use concurrent.futures to execute multiple functions in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit tasks for each website's search function
    flixwave_future = executor.submit(perform_search_and_check_flixwave, search_query)
    flixhq_future = executor.submit(perform_search_and_check_flixhq, search_query)
    fmovies_future = executor.submit(perform_search_and_check_fmovies, search_query)
    nites_future = executor.submit(perform_search_and_check_nites, search_query)
    movies123_future = executor.submit(perform_search_and_check_movies123, search_query)
    movie4kto_future = executor.submit(perform_search_and_check_movie4kto, search_query)
    movies2watch_future = executor.submit(
        perform_search_and_check_movies2watch, search_query
    )
    serieshd_future = executor.submit(perform_search_and_check_serieshd, search_query)
    worthful_future = executor.submit(perform_search_and_check_worthful, search_query)
    watchfreemovies_future = executor.submit(
        perform_search_and_check_watchfreemovies, search_query
    )
    freemoviesfull_future = executor.submit(
        perform_search_and_check_freemoviesfull, search_query
    )
    favhd_future = executor.submit(perform_search_and_check_favhd, search_query)

    # Wait for the tasks to complete
    flixwave_result, flixwave_match = flixwave_future.result()
    flixhq_result, flixhq_match = flixhq_future.result()
    fmovies_result, fmovies_match = fmovies_future.result()
    nites_result, nites_match = nites_future.result()
    movies123_result, movies123_match = movies123_future.result()
    movie4kto_result, movie4kto_match = movie4kto_future.result()
    movies2watch_result, movies2watch_match = movies2watch_future.result()
    serieshd_result, serieshd_match = serieshd_future.result()
    worthful_result, worthful_match = worthful_future.result()
    watchfreemovies_result, watchfreemovies_match = watchfreemovies_future.result()
    freemoviesfull_result, freemoviesfull_match = freemoviesfull_future.result()
    favhd_result, favhd_match = favhd_future.result()

# Process and print the results
if flixwave_result:
    print(f"Similar match found for Flixwave search query '{search_query}':")
    print(f"- {flixwave_match}")
else:
    print(f"No similar match found for Flixwave search query '{search_query}'")

if flixhq_result:
    print(f"Similar match found for flixhq search query '{search_query}':")
    print(f"- {flixhq_match}")
else:
    print(f"No similar match found for flixhq search query '{search_query}'")

if fmovies_result:
    print(f"Similar match found for fmovies search query '{search_query}':")
    print(f"- {fmovies_match}")
else:
    print(f"No similar match found for fmovies search query '{search_query}'")

if nites_result:
    print(f"Similar match found for nites search query '{search_query}':")
    print(f"- {nites_match}")
else:
    print(f"No similar match found for nites search query '{search_query}'")

if movies123_result:
    print(f"Similar match found for movies123 search query '{search_query}':")
    print(f"- {movies123_match}")
else:
    print(f"No similar match found for movies123 search query '{search_query}'")

if movie4kto_result:
    print(f"Similar match found for movie4kto search query '{search_query}':")
    print(f"- {movie4kto_match}")
else:
    print(f"No similar match found for movie4kto search query '{search_query}'")

if movies2watch_result:
    print(f"Similar match found for movie4kto search query '{search_query}':")
    print(f"- {movies2watch_match}")
else:
    print(f"No similar match found for movies2watch search query '{search_query}'")

if serieshd_result:
    print(f"Similar match found for movie4kto search query '{search_query}':")
    print(f"- {serieshd_match}")
else:
    print(f"No similar match found for serieshd search query '{search_query}'")

if worthful_result:
    print(f"Similar match found for worthful search query '{search_query}':")
    print(f"- {worthful_match}")
else:
    print(f"No similar match found for worthful search query '{search_query}'")

if watchfreemovies_result:
    print(f"Similar match found for watchfreemovies search query '{search_query}':")
    print(f"- {watchfreemovies_match}")
else:
    print(f"No similar match found for watchfreemovies search query '{search_query}'")

if freemoviesfull_result:
    print(f"Similar match found for freemoviesfull search query '{search_query}':")
    print(f"- {freemoviesfull_match}")
else:
    print(f"No similar match found for freemoviesfull search query '{search_query}'")

if favhd_result:
    print(f"Similar match found for favhd search query '{search_query}':")
    print(f"- {favhd_match}")
else:
    print(f"No similar match found for favhd search query '{search_query}'")

# Prompt the user to choose a website
website_url, search_box_xpath = prompt_user_for_website()

perform_search_and_open_website(search_query, website_url, search_box_xpath)
