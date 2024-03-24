# Sys(tem Information Viewer)
*Version 1 | 24.03.2024*

The System Information Viewer is a Python application designed to provide a comprehensive overview of your computer's key hardware and software specifications. This easy-to-use tool displays information about the operating system, CPU, GPU, RAM, storage, platform, computer name, and Python version currently in use. The application presents the data in a clear, organized interface with a dark theme for comfortable viewing.

## Features

- **Operating System**: Reveals the name and version of the operating system.
- **CPU Information**: Displays the CPU model and specifications.
- **GPU Information**: Provides the GPU name, applicable for Nvidia GPUs.
- **RAM Speed**: Shows the speed of the RAM installed in MHz.
- **Memory Information**: Includes details about the total, available, used, and free memory, as well as memory utilization percentage.
- **Platform**: Displays detailed platform information.
- **Computer Name**: The name of the computer as recognized on the network.
- **Python Version**: The version of Python that is currently running.

## Installation

Before you can run the System Information Viewer, you need to have the following prerequisites installed on your system:

### Prerequisites

- Python 3.x
- `psutil` library
- `tkinter` library
- `platform` module (usually included with Python)

To install the necessary Python libraries, use the following pip commands: 

```bash
pip install psutil
```

```bash
pip install tkinter
```

```bash
pip install platform
```
_(The order of downloading does not matter)_
## Usage

To run the System Information Viewer, simply clone the repository or download the source code, navigate to the application directory, and execute the script `sys.py`:
```bash
python sys.py
```

## Compatibility

This application is designed for use on Windows operating systems due to the reliance on Windows-specific commands such as `wmic`.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions are welcome to improve the application's functionality, extend support for other operating systems, or enhance the user interface. You can contribute by submitting a [pull request](https://github.com/Johann-FullHD/System-Components-Access-Point/pulls) or reporting bugs and suggestions in the [issue tracker](https://github.com/Johann-FullHD/System-Components-Access-Point/issues). For professional inquiries or potential collaborations, please get in touch via email.


## Contact Information

For any additional questions or feedback, feel free to reach out to me:
- **Johann Kramer**
- **Email**: [kjohann1908@gmail.com](mailto:kjohann1908@gmail.com)
- **Instagram:** [trainspotter.dresden](https://www.instagram.com/trainspotter.dresden/)
