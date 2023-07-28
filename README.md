# College-ERP-System

![ERP System](icon.png)

This College ERP software is designed to manage administrative, faculty, and student activities efficiently. It provides a user-friendly interface and leverages the power of MySQL database to store and retrieve data securely.

## Features

- **Login**: The ERP system allows administrators, faculty, and students to log in securely with their respective credentials.

- **Role-based Access**: Different modules are available based on the user's role (Admin, Faculty, Student) to ensure data privacy and access control.

- **MySQL Database**: The system connects to a remote MySQL database hosted on Clever Cloud to store and manage data effectively.

- **Faculty Dashboard**: Faculty members have access to their information and can view their respective details through an intuitive dashboard.

- **Admin Dashboard**: Administrators can manage the overall system, perform CRUD operations on data, and monitor user activities.

- **Student Dashboard**: Students can view their academic information, timetable, attendance, and other relevant details.

## Requirements

- Python 3.x
- tkinter
- mysql.connector
- webbrowser

## Usage

1. Clone the repository and navigate to the project directory.

2. Ensure you have all the required dependencies installed.

3. Update the database connection credentials in the `connect()` function in the code.

4. Provide the correct URL to your MySQL database in the `login()` function.

5. Run the script by executing `main.py`.

6. Choose your role (Admin, Faculty, or Student) and log in with appropriate credentials.

7. Enjoy the seamless experience of managing college activities!

## Note

- This ERP system is intended for educational purposes and may require further customization for production use.

- Please keep your MySQL credentials secure and do not share them publicly.

- Make sure to maintain backups of your database to avoid data loss.

- The program assumes that the database schema and tables are already set up as per the code implementation.

## Disclaimer

This software is provided as-is without any warranty. Use it responsibly and at your own risk. The developers are not liable for any damages caused by the use or misuse of this ERP system.

For more information, issues, or contributions, please refer to the GitHub repository [link](https://github.com/azim-qadri/College-ERP-System).

**Developers**: [Azim](https://github.com/azim-qadri)

We welcome contributions from the open-source community to enhance features, improve functionality, and make this College ERP software even more efficient and versatile. Feel free to fork the repository and submit your pull requests! Together, let's build a powerful tool for educational institutions.
