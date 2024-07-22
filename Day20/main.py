#!/usr/bin/python3

FINAL_INPUT = """%vb -> ck
%pb -> xv
&gt -> jq
%hj -> lk, hh
%zd -> fm
%hr -> hh
%rg -> tp
%tf -> ck, tx
%pp -> vs, hh
%vx -> df
%tx -> mr, ck
%nh -> vx
%sc -> ck, vb
%cc -> ck, rj
%tn -> kz, lt
%fp -> rb
%hc -> kz
%rb -> ns, mf
%pc -> vh
broadcaster -> tf, br, zn, nc
%zn -> kz, fv
&ns -> pb, lr, br, fp, gp, gv, jl
%nc -> hh, hj
%mf -> ns, gp
%xv -> ns, kh
%rj -> ck, sc
%tg -> cc
%gp -> pb
%jz -> lj, ns
%jl -> fp
&vr -> jq
&jq -> rx
&kz -> zf, nl, df, zn, vx, nh
%gv -> jl
%gf -> zf, kz
%df -> gf
%kq -> pp
%lk -> hh, zd
%vs -> bp
%lt -> ls, kz
&nl -> jq
%mr -> rg
%zf -> qf
%br -> gv, ns
%rk -> hh, hr
%qf -> kz, tn
%rv -> rk, hh
%ls -> hc, kz
%fm -> kq
&ck -> tp, vr, pc, tg, mr, tf, rg
%fv -> nh, kz
%tp -> pc
%vh -> ck, tg
&hh -> vs, kq, gt, nc, zd, fm
&lr -> jq
%kh -> ns, jz
%bp -> hh, rv
%lj -> ns""".split("\n")

TEST_INPUT = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".split("\n")

class Signal:
    def __init__(self, machines, signal=False):
        self.machines = machines
        self.broadcaster = self.machines['broadcaster']
        self.signal = signal
        self.high_sends = 0
        self.low_sends = 0

    def push_button(self, signal=False):
        self.low_sends += 1
        queue = [self.broadcaster]
        while(len(queue) > 0):
            machine = queue.pop(0)
            if(machine.signal):
                self.high_sends += len(machine.connections)
            else:
                self.low_sends += len(machine.connections)
            to_add = machine.send()
            for m in to_add:
                queue.append(m)

class Machine:
    def __init__(self, name, connections):
        self.connections = connections
        self.name = name
        self.signal = False

    def receive(self, machine, signal):
        return True

    def send(self):
        to_send = []
        for machine in self.connections:
            print(f"Sending {self.signal} from {self.name} -> {machine.name}")
            if(machine.receive(self.name, self.signal)):
                to_send.append(machine)
        return to_send

class Broadcaster(Machine):
    def receive(self, machine, signal):
        self.signal = signal
        return True

class FlipFlop(Machine):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.signal = False

    def receive(self, machine, signal):
        if(signal == False):
            self.signal = (not self.signal)
            return True
        return False

class Conjuction(Machine):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.memory = {}
        self.signal = None

    def determine_signal(self):
        for m in self.memory:
            if(self.memory[m] == False):
                return True
        return False

    def receive(self, machine, signal):
        self.memory[machine] = signal
        self.signal = self.determine_signal()
        return True

def build_machines(data):
    machines = {}
    for machine in data:
        machine = machine.split(" -> ")
        connections = machine[1].split(", ")
        match machine[0][0]:
            case "b":
                machines['broadcaster'] = Broadcaster('broadcaster', connections)
            case "%":
                machines[machine[0][1:]] = FlipFlop(machine[0][1:], connections)
            case "&":
                conjuction = Conjuction(machine[0][1:], connections)
                machines[machine[0][1:]] = conjuction
                for line in data:
                    line = line.split(" -> ")
                    if(conjuction.name in line[1]):
                        conjuction.memory[str(line[0][1:])] = False
                conjuction.signal = conjuction.determine_signal()
    return machines

def link_machines(machines):
    for machine in machines:
        new_links = []
        for connection in machines[machine].connections:
            try:
                new_links.append(machines[connection])
            except Exception:
                new_links.append(Broadcaster(connection, []))
        machines[machine].connections = new_links
    return machines

if __name__ == "__main__":
    s = Signal(link_machines(build_machines(FINAL_INPUT)), False)
    for i in range(1000):
        s.push_button()
    print(f"Low Signals: {s.low_sends}\nHigh Signals: {s.high_sends}\nAnswer: {s.high_sends*s.low_sends}")