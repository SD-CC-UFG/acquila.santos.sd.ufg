// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx01;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

import rmiEx01.Servico;
import rmiEx01.ServicoListener;

public class Cliente implements ServicoListener {

	public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
		try {
			String nomeServico = "MeuServico";
			int porta = 54321;

			ServicoListener clienteA = new Cliente();
			ServicoListener clienteAdistribuido = (ServicoListener) UnicastRemoteObject.exportObject(clienteA, 0);

			Registry registry = LocateRegistry.getRegistry(porta);
			Servico servicoRemoto = (Servico) registry.lookup(nomeServico);
			servicoRemoto.addListener(clienteAdistribuido);

                        System.out.println("Informe o nome:");
                        String nome = input.nextLine();
                        System.out.println("Informe o cargo:");
                        String cargo = input.nextLine();
                        System.out.println("Informe o salário atual:");
                        double atualSal = input.nextDouble();
			System.out.println("Cliente enviando: ");
			servicoRemoto.setSalAtual(atualSal);
                        servicoRemoto.setCargo(cargo);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void calculoEfetuado(double resultado) throws RemoteException {
		System.out.println("Novo salário: " + resultado);
	}
}