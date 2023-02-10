# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    instances = [
        (['host_subsystem'], 'ps_router', 'cadence_com::interconnect::vdefault::crouter<32>'),
        (['host_subsystem'], 'core', 'cadence_com::processor::arm::ARMCortexA55x4CT'),
        (['host_subsystem'], 'gic', 'cadence_com::processor::arm::GIC600'),
        (['host_subsystem'], 'loader', 'cadence_com::interface::vdefault::loader'),
        (['host_subsystem'], 'sram', 'cadence_com::memory::vdefault::simple_memory<32>'),
        (['host_subsystem'], 'nor', 'cadence_com::memory::vdefault::simple_memory<32>'),
        (['host_subsystem'], 'ddr_mem', 'cadence_com::memory::vdefault::simple_memory<32>'),
        (['host_subsystem'], 'ethernet', 'cadence_com::peripheral::vdefault::smc91c111_ethernet'),
        (['host_subsystem'], 'slirp_wrapper', 'cadence_com::interface::vdefault::slirp_wrapper'),
        (['host_subsystem'], 'MSIRewriter_SMMU', 'cadence_com::interconnect::arm::MSIRewriter'),
        (['host_subsystem'], 'MSIRewriter_PCIe', 'cadence_com::interconnect::arm::MSIRewriter'),
        (['host_subsystem'], 'MMU_700_1', 'cadence_com::processor::arm::MMU_700'),
        (['host_subsystem'], 'sysctl', 'cadence_com::peripheral::vdefault::sp810_sysctl'),
        (['host_subsystem'], 'reset_gen', 'cadence_com::util::vdefault::pulse_gen'),

        (['host_subsystem'], 'PCIe_RC', 'cadence_com::peripheral::vdefault::pcie'),
        (['device_subsystem'], 'PCIe_EP', 'cadence_com::peripheral::vdefault::pcie'),

        (['device_subsystem'], 'ps_router', 'cadence_com::interconnect::vdefault::crouter<32>'),
        (['device_subsystem'], 'core', 'cadence_com::processor::arm::ARMCortexR52x4CT'),
        (['device_subsystem'], 'reset_gen', 'cadence_com::util::vdefault::pulse_gen'),
        (['device_subsystem'], 'loader', 'cadence_com::interface::vdefault::loader'),
        (['device_subsystem'], 'sram', 'cadence_com::memory::vdefault::simple_memory<32>'),
        (['device_subsystem'], 'nor', 'cadence_com::memory::vdefault::simple_memory<32>'),
        (['device_subsystem'], 'ddr_mem', 'cadence_com::memory::vdefault::simple_memory<32>'),
    ]

    for hpath, inst_name, inst_type in instances:
        print (str(hpath) + ":" + inst_name + ":" + inst_type )


def add_instance(plat, instance_name, instance_ip, inst_dict):
    print("Adding instance :" + plat + ":" + instance_name + ":" + instance_ip + ":" + str(inst_dict))
    # inst_dict[instance_name] = plat.addInstance(instance_name, instance_ip)


def add_stub(plat, instance_name, instance_type, inst_dict):
    print("stubbing :" + plat + ":" + instance_name + ":" + instance_type + ":" + str(inst_dict) )
    # inst_dict[instance_name] = plat.addStub(instance_name, instance_type)

def create_instances(plat):
    inst_dict = dict()
    # Create instances and rename
    add_instance(plat, "a55", "cadence_com::processor::arm::ARMCortexA55x4CT", inst_dict)
    add_instance(plat, "gic600", "cadence_com::processor::arm::GIC600", inst_dict)
    # add_instance(plat, "core", "cadence_com::processor::arm::ARMCortexR52x1CT", inst_dict)

    add_stub(plat, 'unused_debug_s', "initiator_stub<64>", inst_dict)
    add_stub(plat, 'unused_dev_debug_s', "initiator_stub<64>", inst_dict)
    add_stub(plat, 'unused_acp_s', "initiator_stub<64>", inst_dict)
    add_stub(plat, 'unused_snp_socket', "initiator_stub<64>", inst_dict)
    add_stub(plat, 'unused_virtio_s', "initiator_stub<64>", inst_dict)
    add_stub(plat, 'init_socket_auto_stub_1', "target_stub<64>", inst_dict)


    add_instance(plat, "ddram", "cadence_com::memory::vdefault::simple_memory<32>", inst_dict)
    add_instance(plat, "loader", "cadence_com::interface::vdefault::loader", inst_dict)
    add_instance(plat, "sram",  "cadence_com::memory::vdefault::simple_memory<32>", inst_dict)
    #
    add_instance(plat, "pvbus_periph_m_64_32", "cadence_com::interconnect::vdefault::simple_buswidth_converter<64,32>", inst_dict)
    add_instance(plat, "gic_pvbus_m_64_32", "cadence_com::interconnect::vdefault::simple_buswidth_converter<64,32>", inst_dict)
    add_instance(plat, "simple_converter", "cadence_com::interconnect::vdefault::simple_converter", inst_dict)
    add_instance(plat, "pvbus_m_64_32", "cadence_com::interconnect::vdefault::simple_buswidth_converter<64,32>", inst_dict)
    add_instance(plat, "gic_pvbus_s_32_64", "cadence_com::interconnect::vdefault::simple_buswidth_converter<32,64>", inst_dict)


    # check router & sram
    add_instance(plat, "ps_router", "cadence_com::interconnect::vdefault::crouter<32>", inst_dict)
    add_instance(plat, "pl011_uart", "cadence_com::peripheral::vdefault::pl011_uart", inst_dict)
    add_instance(plat, "mspi_0", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "mspi_1", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "mspi_2", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "mspi_3", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "mspi_4", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "mspi_5", "cadence_com::peripheral::mspi::spi", inst_dict)
    add_instance(plat, "rscanfd_0", "cadence_com::peripheral::rscanfd::canfd", inst_dict)
    add_instance(plat, "rscanfd_1", "cadence_com::peripheral::rscanfd::canfd", inst_dict)
    add_instance(plat, "rlin_0", "cadence_com::peripheral::rlin::lin", inst_dict)
    add_instance(plat, "rlin_1", "cadence_com::peripheral::rlin::lin", inst_dict)
    add_instance(plat, "rlin_2", "cadence_com::peripheral::rlin::lin", inst_dict)
    add_instance(plat, "rlin_3", "cadence_com::peripheral::rlin::lin", inst_dict)
    add_instance(plat, "mspi_serial_bus", "cadence_com::interconnect::vdefault::serial_bus", inst_dict)
    add_instance(plat, "canfd_serial_bus", "cadence_com::interconnect::vdefault::serial_bus", inst_dict)
    add_instance(plat, "rlin_serial_bus", "cadence_com::interconnect::vdefault::serial_bus", inst_dict)
    add_instance(plat, "rlin_ttymonitor", "cadence_com::interface::vdefault::ttymonitor", inst_dict)
    add_instance(plat, "uart_ttymonitor", "cadence_com::interface::vdefault::ttymonitor", inst_dict)
    add_instance(plat, "uart_term", "cadence_com::interface::vdefault::term", inst_dict)
    add_instance(plat, "rlin_term", "cadence_com::interface::vdefault::term", inst_dict)

    add_instance(plat, "flexray_0", "cadence_com::peripheral::rflxa::flexray", inst_dict)
    add_instance(plat, "rsent_0", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_1", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_2", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_3", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_4", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_5", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_6", "cadence_com::peripheral::rsent::sent", inst_dict)
    add_instance(plat, "rsent_7", "cadence_com::peripheral::rsent::sent", inst_dict)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    create_instances("platform")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
