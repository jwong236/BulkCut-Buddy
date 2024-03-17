//
//  enter_data.swift
//  bulk
//
//  Created by Ryan on 3/13/24.
//

import SwiftUI

struct enter_data: View {
    @State private var showingPredictionData = false
    @State private var goal = ""
    @State private var calorie_intake = ""
    @State private var calories_burned = ""
    @State private var protein_intake = ""
    @State private var steps_taken = ""
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
                    TextField("Goal: (bulking/cutting)", text: $goal)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Calories consumed", text: $calorie_intake)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Calories burned (exercise)", text: $calories_burned)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Protein intake (g)", text: $protein_intake)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    TextField("Steps taken", text: $steps_taken)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(10)
                    Button("Enter") {
                        showingPredictionData = true
                    }
                    .foregroundColor(.white)
                    .frame(width: 300, height: 50)
                    .background(Color.blue)
                    .cornerRadius(10)
                    
                    NavigationLink(destination: prediction(goal: .constant(goal.lowercased()), c_in: .constant(Double(calorie_intake) ?? 0), c_out: .constant(Double(calories_burned) ?? 0), protein: .constant(Double(protein_intake) ?? 0), steps: .constant(Double(steps_taken) ?? 0)), isActive: $showingPredictionData) {
                        EmptyView()
                    }
                }
            }
        }
        
    }
}

#Preview {
    enter_data()
}
