# RCM-ENGINEERING

## Project Overview
RCM-ENGINEERING is a dedicated platform for the RCM team, composed of engineering students committed to providing free summaries of engineering materials. The project aims to facilitate learning and improve academic performance for engineering students by offering easily accessible educational resources.

### Importance of the Project
This project addresses the significant need for accessible educational materials in the engineering field. By creating a collaborative platform, we enable students to share knowledge and resources effectively. The initiative not only supports students in their studies but also fosters a sense of community among aspiring engineers.

## Main Pages
The website consists of several key pages, each serving a specific purpose:

1. **Home Page**: Welcomes new visitors and introduces them to the team's activities and goals.
2. **Summaries Page**: Displays all available summaries with options to search and filter by subject.
3. **Team Members Page**: Provides general information about the members of the RCM engineering team.
4. **Blog Page**: Publishes articles and posts related to engineering, aimed at supporting first-year engineering students.
5. **Contact Page**: Offers a means of communication with the team for students needing specific summaries or support.
6. **Profile Page**: Displays the user's profile information.

## Team Collaboration and Summary Sharing
To enhance collaboration, the platform allows users to submit summaries, which are then reviewed and approved by team members before being published. This peer-review process ensures high-quality content and promotes shared learning experiences.

## Integrated Applications
The project comprises the following applications:
- **authentication**: Manages user registration and login.
- **blog**: Handles blog content management.
- **engineering_summaries**: Manages engineering summaries submissions and display.
- **main**: Contains core site components.
- **ourteam**: Manages team member information.
- **project**: Oversees team projects.
- **static**: Stores static files (CSS, JS, images).
- **templates**: Holds HTML templates used throughout the site.

## Running the Project
To run the RCM-ENGINEERING project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/salahsaeed19/RCM-ENGINEERING.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd RCM-ENGINEERING
   ```

3. **Install Requirements**:
   Make sure you have `pip` installed and then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**:
   Run the following commands to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   To access the admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   Finally, start the development server:
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**:
   Open your web browser and go to `http://127.0.0.1:8000/` to view the site.

## Contribution
If you'd like to contribute to the development of this project, please feel free to open issues or pull requests on our GitHub repository.

## Contact Information
For any inquiries or support requests, please reach out to the RCM team through the contact page on the website.

## Notes
This project aims to empower engineering students by providing them with easy access to educational materials and fostering a collaborative learning environment. Your participation and feedback are valuable to us as we strive to improve the platform and support the engineering community.
