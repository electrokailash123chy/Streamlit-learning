#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cctype>
#include <regex>

#ifdef _WIN32
    #define CLEAR_COMMAND "cls"
    #include <windows.h> // For colors on Windows
#else
    #define CLEAR_COMMAND "clear"
#endif

using namespace std;

// Color codes for console (cross-platform)
#ifdef _WIN32
    enum Color { BLACK = 0, BLUE = 1, GREEN = 2, CYAN = 3, RED = 4, MAGENTA = 5, YELLOW = 6, WHITE = 7, DARK_YELLOW = 14, LIGHT_GRAY = 8, LIGHT_CYAN = 11 };
    void setColor(int color) {
        HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
        SetConsoleTextAttribute(hConsole, color);
    }
#else
    void setColor(const string& color) { cout << color; }
    const string RESET = "\033[0m";
    const string RED = "\033[31m";
    const string GREEN = "\033[32m";
    const string YELLOW = "\033[33m";
    const string BLUE = "\033[34m";
    const string MAGENTA = "\033[35m";
    const string CYAN = "\033[36m";
    const string WHITE = "\033[37m";
    const string DARK_YELLOW = "\033[33m";
    const string LIGHT_GRAY = "\033[90m";
    const string LIGHT_CYAN = "\033[96m";
#endif

// Class to hold contact information
class Contact {
private:
    string name;
    string phone;
    string email;

public:
    Contact(string n = "Unknown", string p = "0000000000", string e = "unknown@none.com")
        : name(n), phone(p), email(e) {}
   
    string getName() const { return name; }
    string getPhone() const { return phone; }
    string getEmail() const { return email; }
   
    void setName(string n) { name = (n == "-" ? "Unknown" : n); }
    void setPhone(string p) { phone = (p == "-" ? "0000000000" : p); }
    void setEmail(string e) { email = (e == "-" ? "unknown@none.com" : e); }
   
    string toString() const { return name + ":" + phone + ":" + email; }
};

// Regex validation
bool isValidPhone(const string& input) {
    regex phoneRegex(R"(^\d{10,15}$)");
    string digits = input == "-" ? "0000000000" : input;
    for (char& c : digits) if (!isdigit(c)) return false;
    return regex_match(digits, phoneRegex);
}

bool isValidEmail(const string& input) {
    regex emailRegex(R"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)");
    return input == "-" || regex_match(input, emailRegex);
}

// Improved field detection
bool isPhone(const string& input) { return isValidPhone(input); }
bool isEmail(const string& input) { return isValidEmail(input) && input.find('@') != string::npos; }
bool isName(const string& input) { return !isPhone(input) && !isEmail(input) && !input.empty() && input != "-"; }

// Load contacts from the last DATA_SECTION
vector<Contact> loadContacts() {
    vector<Contact> contacts;
    ifstream file(__FILE__);
    vector<string> lines;
    string line;
   
    while (getline(file, line)) lines.push_back(line);
    file.close();

    for (int i = lines.size() - 1; i >= 0; i--) {
        if (lines[i].find("// DATA_SECTION") != string::npos) {
            for (int j = i + 1; j < lines.size(); j++) {
                if (lines[j].find("// ") == 0) {
                    string entry = lines[j].substr(3);
                    size_t pos1 = entry.find(':');
                    size_t pos2 = entry.find(':', pos1 + 1);
                    if (pos1 != string::npos && pos2 != string::npos) {
                        Contact contact;
                        contact.setName(entry.substr(0, pos1));
                        contact.setPhone(entry.substr(pos1 + 1, pos2 - pos1 - 1));
                        contact.setEmail(entry.substr(pos2 + 1));
                        contacts.push_back(contact);
                    }
                }
            }
            break;
        }
    }
    return contacts;
}

// Save contacts to file
void saveContacts(const vector<Contact>& contacts) {
    ifstream inFile(__FILE__);
    stringstream buffer;
    vector<string> lines;
    string line;

    while (getline(inFile, line)) lines.push_back(line);
    inFile.close();

    int lastDataSection = -1;
    for (int i = lines.size() - 1; i >= 0; i--) {
        if (lines[i].find("// DATA_SECTION") != string::npos) {
            // if(lines[i]=="// DATA_SECTION")
            lastDataSection = i;
            break;
        }
    }

    if (lastDataSection == -1) {
        for (const auto& l : lines) buffer << l << "\n";
        buffer << "// DATA_SECTION\n";
    } else {
        for (int i = 0; i <= lastDataSection; i++) buffer << lines[i] << "\n";
    }

    buffer << "// Add your contacts below this line as comments in format: // name:phone:email\n";
    for (const auto& contact : contacts) {
        buffer << "// " << contact.toString() << "\n";
    }

    ofstream outFile(__FILE__);
    outFile << buffer.str();
    outFile.close();
}

// Display contacts with an ASCII table and subtle colors
void displayContacts(const vector<Contact>& contacts) {
    if (contacts.empty()) {
        setColor(YELLOW); cout << "Phonebook is empty!" << endl; setColor(WHITE);
        return;
    }
    setColor(LIGHT_CYAN);
    cout << "\n+--------------------------------+---------------------+---------------------+" << endl;
    cout << "|                            PHONEBOOK CONTACTS                              |" << endl;
    cout << "+--------------------------------+---------------------+---------------------+" << endl;
    cout << "|            NAME                |       PHONE         |       EMAIL         |" << endl;
    cout << "+--------------------------------+---------------------+---------------------+" << endl;
    setColor(WHITE);
    for (const auto& contact : contacts) {
        cout << "| " << left << setw(30) << contact.getName().substr(0, 30) << " | "
             << setw(19) << contact.getPhone().substr(0, 19) << " | "
             << setw(19) << contact.getEmail().substr(0, 19) << " |" << endl;
    }
    setColor(LIGHT_CYAN);
    cout << "+--------------------------------+---------------------+---------------------+" << endl;
    setColor(WHITE);
}

// Search contacts
void searchContacts(const vector<Contact>& contacts, const string& query) {
    bool found = false;
    for (const auto& contact : contacts) {
        if (contact.getName().find(query) != string::npos ||
            contact.getPhone().find(query) != string::npos ||
            contact.getEmail().find(query) != string::npos) {
            setColor(GREEN);
            cout << contact.getName() << " - " << contact.getPhone() << " - " << contact.getEmail() << endl;
            setColor(WHITE);
            found = true;
        }
    }
    if (!found) {
        setColor(YELLOW); cout << "No matching contacts found!" << endl; setColor(WHITE);
    }
}

// Delete contact
void deleteContact(vector<Contact>& contacts, const string& query) {
    vector<Contact> newContacts;
    bool found = false;
    for (const auto& contact : contacts) {
        if (contact.getName() != query && contact.getPhone() != query && contact.getEmail() != query) {
            newContacts.push_back(contact);
        } else found = true;
    }
    if (found) {
        contacts = newContacts;
        saveContacts(contacts);
        setColor(GREEN); cout << "Contact deleted permanently!" << endl; setColor(WHITE);
    } else {
        setColor(YELLOW); cout << "Contact not found!" << endl; setColor(WHITE);
    }
}

// Check for duplicate names
bool hasDuplicateName(const vector<Contact>& contacts, const string& name) {
    if (name == "Unknown") return false;
    for (const auto& contact : contacts) {
        if (contact.getName() == name) return true;
    }
    return false;
}

// Add contact with flexible parameters
void addContact(vector<Contact>& contacts, const vector<string>& params) {
    if (params.empty()) {
        setColor(RED); cout << "Please provide at least one parameter!" << endl; setColor(WHITE);
        return;
    }

    string name, phone, email;
    vector<string> unassigned;

    for (const auto& param : params) {
        if (isPhone(param)) phone = param;
        else if (isEmail(param)) email = param;
        else unassigned.push_back(param);
    }

    if (!unassigned.empty()) {
        name = unassigned[0];
        for (size_t i = 1; i < unassigned.size(); i++) {
            if (!isPhone(unassigned[i]) && !isEmail(unassigned[i])) {
                name += " " + unassigned[i];
            }
        }
    }

    if (name.empty()) name = "-";
    if (phone.empty()) phone = "-";
    if (email.empty()) email = "-";

    if (hasDuplicateName(contacts, name)) {
        setColor(YELLOW); cout << "Record with name '" << name << "' already exists!" << endl; setColor(WHITE);
        return;
    }
    if (!isValidPhone(phone)) {
        setColor(RED); cout << "Invalid phone number! Must be 10-15 digits." << endl; setColor(WHITE);
        return;
    }
    if (!isValidEmail(email)) {
        setColor(RED); cout << "Invalid email format!" << endl; setColor(WHITE);
        return;
    }

    Contact newContact;
    newContact.setName(name);
    newContact.setPhone(phone);
    newContact.setEmail(email);
    contacts.push_back(newContact);
    saveContacts(contacts);
    setColor(GREEN); cout << "Contact added!" << endl; setColor(WHITE);
}

// Sort contacts
void sortContacts(vector<Contact>& contacts) {
    sort(contacts.begin(), contacts.end(),
         [](const Contact& a, const Contact& b) { return a.getName() < b.getName(); });
    saveContacts(contacts);
    setColor(GREEN); cout << "Contacts sorted alphabetically!" << endl; setColor(WHITE);
}

// Display home page
void displayHome() {
    system(CLEAR_COMMAND);
    setColor(LIGHT_CYAN);
    cout << "+------------------------------------------+" << endl;
    cout << "|       Welcome to Phonebook CLI           |" << endl;
    cout << "|     Developed by: @Upendra237            |" << endl;
    cout << "|   First Release: February 20, 2025       |" << endl;
    cout << "+------------------------------------------+" << endl;
    setColor(WHITE);
    cout << "\nFeatures:\n";
    setColor(DARK_YELLOW);
    cout << "  * Add contacts with name, phone, email (auto-detected)\n";
    cout << "  * Delete by name, phone, or email\n";
    cout << "  * Search across all fields\n";
    cout << "  * Beautiful table display\n";
    cout << "  * Sort alphabetically\n";
    cout << "  * Use '-' for optional fields\n";
    cout << "  * All contacts saved within the .cpp file\n";
    setColor(LIGHT_GRAY);
    cout << "\nType 'help' for commands\n";
    setColor(WHITE);
}

// Parse input allowing flexible order and spaces in name
vector<string> parseInput(const string& input, string& command) {
    vector<string> params;
    stringstream ss(input);
    ss >> command;
    string param;
    while (getline(ss >> ws, param, ' ')) {
        if (!param.empty()) {
            if (param.front() == '"' && param.back() != '"') {
                string rest;
                getline(ss, rest, '"');
                param = param.substr(1) + " " + rest;
            } else if (param.front() == '"' && param.back() == '"') {
                param = param.substr(1, param.length() - 2);
            }
            params.push_back(param);
        }
    }
    return params;
}

int main() {
    vector<Contact> contacts = loadContacts();
    string input, command;

    displayHome();

    while (true) {
        setColor(MAGENTA); cout << "Phonebook> "; setColor(WHITE);
        getline(cin, input);
       
        vector<string> params = parseInput(input, command);
        transform(command.begin(), command.end(), command.begin(), ::tolower);
        if (command == "add" && !params.empty()) {
            addContact(contacts, params);
        } else if (command == "delete" && !params.empty()) {
            deleteContact(contacts, params[0]);
        } else if (command == "cls") {
            system(CLEAR_COMMAND);
        } else if (command == "search" && !params.empty()) {
            searchContacts(contacts, params[0]);
        } else if (command == "list") {
            displayContacts(contacts);
        } else if (command == "sort") {
            sortContacts(contacts);
        } else if (command == "home") {
            displayHome();
        } else if (command == "help") {
            setColor(LIGHT_CYAN);
            cout << "\n+------------------+------------------------------------------+" << endl;
            cout << "| Command          | Description                              |" << endl;
            cout << "+------------------+------------------------------------------+" << endl;
            setColor(WHITE);
            cout << "| 1. add           | Add a new contact (any order)            |" << endl;
            cout << "| 2. delete        | Delete by name, phone, or email          |" << endl;
            cout << "| 3. search        | Search across all fields                 |" << endl;
            cout << "| 4. list          | Show all contacts                        |" << endl;
            cout << "| 5. sort          | Sort alphabetically                      |" << endl;
            cout << "| 6. home          | Show home page                           |" << endl;
            cout << "| 7. cls           | Clear screen                             |" << endl;
            cout << "| 8. exit          | Quit program                             |" << endl;
            setColor(LIGHT_CYAN);
            cout << "+------------------+------------------------------------------+" << endl;
            setColor(LIGHT_GRAY);
            cout << "Note: Use '-' for optional fields (e.g., add Ram - ram@example.com)\n";
            setColor(WHITE);
        } else if (command == "exit") {
            setColor(GREEN); cout << "Goodbye!" << endl; setColor(WHITE);
            break;
        } else {
            setColor(RED); cout << "Invalid command! Type 'help' for available commands." << endl; setColor(WHITE);
        }
    }

    return 0;
}































































































































































































































































































































































































































// DATA_SECTION
// Add your contacts below this line as comments in format: // name:phone:email
// 88888888 none:0000000000:unknown@none.com
// 999999999 none:0000000000:unknown@none.com
// Aaditya:0000000000:unknown@none.com
// Add your contacts below this line as comments in format: // name:phone:email
// Kailash:9749823513:unknown@none.com
// Reni:9864111421:unknown@none.com
// Sanjib Kasti:9864163280:sanjibkasti@gmail.com
// Upendra:0000000000:unknown@none.com
// none:7777777777:unknown@none.com

