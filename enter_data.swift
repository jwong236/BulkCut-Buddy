//
//  enter_data.swift
//  bulk
//
//  Created by Ryan on 3/13/24.
//

import SwiftUI

struct enter_data: View {
    @State private var calorie_intake = ""
    @State private var calories_burned = ""
    @State private var protein_intake = ""
    var body: some View {
        NavigationStack {
            ZStack {
                Color.blue
                    .ignoresSafeArea()
                Circle()
                    .scale(1.7)
                    .foregroundColor(.white.opacity(0.15))
                Circle()
                    .scale(1.35)
                    .foregroundColor(.white)
                VStack {
                    Text("Data Entry")
                        .font(.largeTitle)
                        .bold()
                        .padding()
                    TextField("Calories consumed", text: $calorie_intake)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Calories burned", text: $calories_burned)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Protein intake (g)", text: $protein_intake)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    Button("Enter") {
                        push_data(calorie_intake: calorie_intake, calories_burn: calories_burned, protein_intake: protein_intake)
                    }
                    .foregroundColor(.white)
                    .frame(width: 300, height: 50)
                    .background(Color.blue)
                    .cornerRadius(10)
                }
            }
        }
        
    }
    func push_data(calorie_intake: String, calories_burn: String, protein_intake: String) {
        //converting the strings to ints
        let c_in = Int(calorie_intake) ?? 0
        let c_burn = Int(calories_burn) ?? 0
        let p_in = Int(protein_intake) ?? 0
        //YOUR CODE HERE
        //
        //
        //
        //
        
    }
    
}

#Preview {
    enter_data()
}
