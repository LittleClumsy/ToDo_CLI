# Exit codes

<table>
    <tr>
        <th>Code</th>
        <th>Description</th>
        <th>More Info</th>
    </tr>
    <tr>
        <td>0</td>
        <td>Success/No errors</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>Storage Directory Installation Failure</td>
        <td>This error will only occur if the directory installation failed. This will most likely happen because if the OS is not supported or if important code has been removed from the install process.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>JSON Error</td>
        <td>This error will only happen if there was an attempt to write invalid json to a file, or if there was an attempt to read invalid json. NOTE: We consider anything that cannot be converted to a dictionary or a list as invalid json. We understand that is not strictly true but that is the limitation.</td>
    </tr>
</table>