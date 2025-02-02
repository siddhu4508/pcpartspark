def check_compatibility(components):
    errors = []
    cpu = next((c for c in components if c.category == 'CPU'), None)
    gpu = next((c for c in components if c.category == 'GPU'), None)
    ram = next((c for c in components if c.category == 'RAM'), None)
    mobo = next((c for c in components if c.category == 'MOBO'), None)
    psu = next((c for c in components if c.category == 'PSU'), None)
    storage = next((c for c in components if c.category == 'Storage'), None)
    case = next((c for c in components if c.category == 'Case'), None)
    monitor = next((c for c in components if c.category == 'Monitor'), None)
    keyboard = next((c for c in components if c.category == 'Keyboard'), None)
    mouse = next((c for c in components if c.category == 'Mouse'), None)
    headset = next((c for c in components if c.category == 'Headset'), None)
    software = next((c for c in components if c.category == 'Software'), None)

    if cpu and mobo:
        if cpu.specs['socket'] != mobo.specs['socket']:
            errors.append('CPU and Motherboard are not compatible')

    if gpu and psu:
        if gpu.specs['power'] > psu.specs['wattage']:
            errors.append('GPU and PSU are not compatible')

    if ram and mobo:
        if ram.specs['type'] != mobo.specs['memory_type']:
            errors.append('RAM and Motherboard are not compatible')

    if storage and mobo:
        if storage.specs['interface'] != mobo.specs['storage_interface']:
            errors.append('Storage and Motherboard are not compatible')

    if case and cpu:
        if case.specs['size'] != cpu.specs['case_size']:
            errors.append('Case and CPU are not compatible')    

    if case and psu:
        if case.specs['size']!= psu.specs['case_size']:
            errors.append('Case and PSU are not compatible')

    if case and storage:
        if case.specs['size'] != storage.specs['case_size']:
            errors.append('Case and Storage are not compatible')

    if case and ram:
        if case.specs['size'] != ram.specs['case_size']:
            errors.append('Case and RAM are not compatible')

    if case and gpu:
        if case.specs['size'] != gpu.specs['case_size']:
            errors.append('Case and GPU are not compatible')
    

    if case and mobo:
        if case.specs['size'] != mobo.specs['case_size']:
            errors.append('Case and Motherboard are not compatible')
    

    if monitor and gpu:
        if monitor.specs['resolution'] != gpu.specs['resolution']:
            errors.append('Monitor and GPU are not compatible')

    if keyboard and software:
        if keyboard.specs['type'] != software.specs['keyboard_type']:
            errors.append('Keyboard and Software are not compatible')

    if mouse and software:
        if mouse.specs['type'] != software.specs['mouse_type']:
            errors.append('Mouse and Software are not compatible')

    if headset and software:
        if headset.specs['type'] != software.specs['headset_type']:
            errors.append('Headset and Software are not compatible')
