from datetime import datetime
from typing import Dict, List, Optional

from python_on_whales.utils import DockerCamelModel


class PodInfraConfig(DockerCamelModel):
    port_bindings: Optional[Dict[...]] = None
    host_network: Optional[bool] = None
    static_ip: Optional[str] = None
    static_mac: Optional[str] = None
    no_manage_resolv_conf: Optional[bool] = None
    dns_server: Optional[...] = None
    dns_search: Optional[...] = None
    dns_option: Optional[...] = None
    no_manage_hosts: Optional[bool] = None
    host_add: Optional[...] = None
    networks: Optional[...] = None
    network_options: Optional[...] = None
    pid_ns: Optional[str] = None
    userns: Optional[str] = None
    uts_ns: Optional[str] = None


class PodContainer(DockerCamelModel):
    id: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None


class PodInspectResult(DockerCamelModel):
    id: Optional[str] = None
    name: Optional[str] = None
    created: Optional[datetime] = None
    create_command: Optional[List[str]] = None
    exit_policy: Optional[str] = None
    state: Optional[str] = None
    hostname: Optional[str] = None
    create_cgroup: Optional[bool] = None
    cgroup_parent: Optional[str] = None
    cgroup_path: Optional[str] = None
    create_infra: Optional[bool] = None
    infra_container_id: Optional[str] = None
    infra_config: Optional[PodInfraConfig] = None
    shared_namespaces: Optional[List[str]] = None
    num_containers: Optional[int] = None
    containers: Optional[List[PodContainer]] = None
