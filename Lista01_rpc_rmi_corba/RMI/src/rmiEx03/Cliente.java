// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx03;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

public class Cliente implements ServicoListener {

	public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
		try {
			String nomeServico = "MeuServico";
			int porta = 12345;

			ServicoListener clienteA = new Cliente();
			ServicoListener clienteAdistribuido = (ServicoListener) UnicastRemoteObject.exportObject(clienteA, 0);

			Registry registry = LocateRegistry.getRegistry(porta);
			Servico servicoRemoto = (Servico) registry.lookup(nomeServico);
			servicoRemoto.addListener(clienteAdistribuido);

                        System.out.println("Informe a nota 1:");
                        double N1 = input.nextDouble();
                        System.out.println("Informe a nota 2:");
                        double N2 = input.nextDouble();
                        System.out.println("Informe a nota 3:");
                        double N3 = input.nextDouble();
			System.out.println("Cliente enviando: ");
			servicoRemoto.setN1(N1);
                        servicoRemoto.setN2(N2);
                        servicoRemoto.setN3(N3);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void calculoEfetuado(String resultado) throws RemoteException {
		System.out.println("Resultado: " + resultado);
	}
}