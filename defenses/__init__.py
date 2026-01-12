from .strategies import (
    # Base
    DefenseStrategy,
    NoDefense,
    # Phase 1 defenses
    InputSanitizer,
    InstructionEmphasis,
    ExplicitDefenseClause,
    XMLDelimiting,
    SandwichDefense,
    OutputValidator,
    LayeredDefense,
    MaximumDefense,
    # Phase 2 defenses
    SummarizerDefense,
    SentimentDefense,
    Phase2InputSanitizer,
    Phase2LayeredDefense,
    MaximumPhase2Defense,
    # Utility functions
    get_all_defenses,
    get_phase2_defenses,
    get_defense_by_name,
)
