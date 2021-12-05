class DiagnosticReport
    attr_reader :diag_length, :gamma, :epsilon, :oxygen, :co2
    def initialize
        @diags = File.readlines('input.txt').map(&:chomp)
        @diag_length = @diags[0].length
        @gamma = ''
        @epsilon = ''
        @oxygen = @diags.clone
        @co2 = @diags.clone
    end

    def calc_gamma(pos)
        zeros = 0
        ones = 0
        @diags.each { |diag| if diag[pos] == '0' 
            zeros += 1 
        else 
            ones += 1
        end }
        if zeros > ones
            @gamma += '0'
        else
            @gamma += '1'
        end
    end

    def calc_epsilon(pos)
        zeros = 0
        ones = 0
        @diags.each { |diag| if diag[pos] == '0' 
            zeros += 1 
        else 
            ones += 1
        end }
        if zeros > ones
            @epsilon += '1'
        else
            @epsilon += '0'
        end
    end
    
    def calc_oxygen(pos)
        return if @oxygen.length == 1
        zeros = 0
        ones = 0
        @oxygen.each { |o| if o[pos] == '0'
            zeros += 1
        else
            ones += 1
        end }
        if zeros > ones
            @oxygen.delete_if { |o| o[pos] != '0' }
        else
            @oxygen.delete_if { |o| o[pos] != '1' }
        end
    end

    def calc_co2(pos)
        return if @co2.length == 1
        zeros = 0
        ones = 0
        @co2.each { |c| if c[pos] == '0'
            zeros += 1
        else
            ones += 1
        end }
        if zeros > ones
            @co2.delete_if { |c| c[pos] != '1' }
        else
            @co2.delete_if { |c| c[pos] != '0' }
        end
    end
end

def part1
    diag_report = DiagnosticReport.new
    (0...diag_report.diag_length).each { |p| diag_report.calc_gamma(p)
                                             diag_report.calc_epsilon(p) }
    puts diag_report.gamma.to_i(2) * diag_report.epsilon.to_i(2)
end

def part2
    diag_report = DiagnosticReport.new
    (0...diag_report.diag_length).each { |p| diag_report.calc_oxygen(p)
                                            diag_report.calc_co2(p) }
    puts diag_report.oxygen[0].to_i(2) * diag_report.co2[0].to_i(2)
end

part1
part2